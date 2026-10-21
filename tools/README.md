# Tools Inventory | جرد الأدوات

> ⬜ لم يثبت · 🟨 مثبت/يتعلم · ✅ يتقنه
> كل الأدوات مجانية أو فيها نسخة تجريبية/مجتمعية.

## Lab infrastructure (اللابتوب)
| الأداة | الاستخدام | Phase | الحالة |
|---|---|---|---|
| VirtualBox أو VMware Workstation Pro (مجاني للاستخدام الشخصي) | تشغيل الـ VMs | 0 | ⬜ |
| GNS3 أو EVE-NG Community | محاكاة شبكات/switches | 1 | ⬜ |
| Ubuntu Server / Kali Linux | attacker + أدوات | 0 | ⬜ |
| WSL2 (Ubuntu) | Linux سريع على Windows | 0 | ⬜ |

## Networking & Firewalls
| الأداة | الاستخدام | Phase | الحالة |
|---|---|---|---|
| pfSense / OPNsense | firewall مجاني للاب | 1 | ⬜ |
| FortiGate VM (trial / permanent eval) | نفس اللي يستخدمونه زملاؤك | 1 | ⬜ |
| Wireshark | تحليل الترافيك | 0 | 🟨 |
| Nmap | discovery (بحذر في OT!) | 0 | ⬜ |

## Identity
| الأداة | الاستخدام | Phase | الحالة |
|---|---|---|---|
| Windows Server (Evaluation 180 يوم) | Active Directory، GPO | 2 | ⬜ |
| FreeRADIUS أو Windows NPS | مصادقة الأجهزة | 2 | ⬜ |

## Logging & Detection
| الأداة | الاستخدام | Phase | الحالة |
|---|---|---|---|
| rsyslog | syslog server | 3 | ⬜ |
| Wazuh | SIEM + endpoint agent | 3 | ⬜ |
| Security Onion | Zeek + Suricata + analysis | 5 | ⬜ |
| Zeek + ICSNPP parsers (CISA) | تحليل Modbus/DNP3/104 | 5 | ⬜ |
| Malcolm (CISA) | منصة تحليل pcaps للـ ICS | 5 | ⬜ |

## OT protocols & simulation
| الأداة | الاستخدام | Phase | الحالة |
|---|---|---|---|
| pymodbus (Python) | Modbus server/client | 0 | ⬜ |
| libiec61850 | MMS server/client، GOOSE publisher/subscriber | 5 | ⬜ |
| lib60870 | IEC 104 | 5 | ⬜ |
| OpenDNP3 / pydnp3 | DNP3 | 5 | ⬜ |
| Scapy | صناعة packets (GOOSE، ARP) | 5 | ⬜ |

## Study
| الأداة | الاستخدام |
|---|---|
| Professor Messer (مجاني، YouTube) | فيديوهات Security+ لكل objective |
| `review/question-bank.md` | أسئلة مع Claude |
| CISA ICS advisories | ثغرات حقيقية في أجهزة صناعية |

## Scripts (في هذا المجلد)
كل سكربت نكتبه للاستخدام المتكرر يجي هنا مع شرح.
