"""
Lab 00 - observer client.

Connects to the local simulated RTU and READS its state, the way a legitimate
HMI or an OT monitoring tool (Nozomi/Claroty) would. Read-only.

The teaching point: this client needed no username, no password, no key.
Modbus/TCP has no authentication layer at all. A read tool and a write tool
are the same tool with a different function code -- which is exactly why
network segmentation and access control have to live OUTSIDE the protocol.

Run the RTU first (python rtu_sim.py), then:  python observe_client.py
"""
from pymodbus.client import ModbusTcpClient

HOST, PORT = "127.0.0.1", 5020


def main():
    client = ModbusTcpClient(HOST, port=PORT)
    client.connect()  # no credentials requested or required

    coil = client.read_coils(address=0, count=1)
    regs = client.read_holding_registers(address=0, count=3)

    print("Connected with zero authentication.\n")
    print(f"  CB-101 breaker : {'CLOSED' if coil.bits[0] else 'OPEN'}")
    print(f"  Feeder current : {regs.registers[0]} A")
    print(f"  Bus voltage    : {regs.registers[1] / 10:.1f} kV")
    print(f"  OC trip setting: {regs.registers[2]} A")

    client.close()


if __name__ == "__main__":
    main()
