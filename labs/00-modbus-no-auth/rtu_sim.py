"""
Lab 00: Simulated substation RTU speaking Modbus/TCP.

Coil 0          = Breaker CB-101 status   (1 = CLOSED, 0 = OPEN)
Holding reg 0   = Feeder current (A)
Holding reg 1   = Bus voltage (V/10, e.g. 1320 = 132.0 kV)
Holding reg 2   = Over-current trip setting (A)

There is NO authentication: anyone who can reach TCP/5020 can read AND write.
Run:  python rtu_sim.py
"""
import asyncio
import logging

from pymodbus.datastore import (
    ModbusDeviceContext,
    ModbusSequentialDataBlock,
    ModbusServerContext,
)
from pymodbus.server import StartAsyncTcpServer

logging.basicConfig(format="%(asctime)s [RTU] %(message)s", level=logging.INFO)
log = logging.getLogger()

HOST, PORT = "127.0.0.1", 5020  # 502 is the real port; 5020 avoids needing admin rights

# Initial plant state. In pymodbus 3.16 the block's start address must be >= 1;
# it maps internally so that Modbus address 0 is the first value below.
coils = ModbusSequentialDataBlock(1, [1] + [0] * 9)                 # addr 0: breaker CLOSED
registers = ModbusSequentialDataBlock(1, [412, 1320, 800] + [0] * 7)  # addr 0,1,2

device = ModbusDeviceContext(co=coils, hr=registers)
context = ModbusServerContext(devices=device, single=True)


async def watch_plant():
    """Print the plant state every 2 s so you can SEE the attack land."""
    last = None
    while True:
        breaker = device.getValues(1, 0, 1)[0]          # fc 1 = coils
        current, voltage, setting = device.getValues(3, 0, 3)  # fc 3 = holding regs
        state = (breaker, current, voltage, setting)
        if state != last:
            log.info(
                "CB-101=%s | I=%sA | V=%.1fkV | OC setting=%sA",
                "CLOSED" if breaker else "OPEN  ", current, voltage / 10, setting,
            )
            last = state
        await asyncio.sleep(2)


async def main():
    log.info("RTU listening on %s:%s (no authentication!)", HOST, PORT)
    asyncio.create_task(watch_plant())
    await StartAsyncTcpServer(context=context, address=(HOST, PORT))


if __name__ == "__main__":
    asyncio.run(main())
