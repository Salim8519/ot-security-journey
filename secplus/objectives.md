# Security+ Objectives ↔ OT Labs

> مبني على أهداف **SY0-701**. لو قررنا نختبر **SY0-801** نحدّث الجدول (المفاهيم تقريباً نفسها، الأوزان تختلف شوي).
> Status: ⬜ not started · 🟨 in progress · ✅ done · 🔁 needs review

## Domain 1: General Security Concepts (12%)
| # | Objective | الزاوية OT | Phase / Lab | Status |
|---|---|---|---|---|
| 1.1 | Security controls (technical, managerial, operational, physical; preventive, detective…) | controls في المحطة: firewall، أقفال الكبائن، إجراءات الدخول | P0 | ⬜ |
| 1.2 | Fundamental concepts: CIA, AAA, Zero Trust, physical security, deception | في OT الأولوية Availability ثم Integrity ثم Confidentiality | P0 / Lab 00 | ⬜ |
| 1.3 | Change management | تغيير setting في relay = change management | P4 | ⬜ |
| 1.4 | Cryptographic solutions (PKI, hashing, TLS, keys) | IEC 62351 (TLS للـ MMS، توقيع GOOSE) | P5 | ⬜ |

## Domain 2: Threats, Vulnerabilities & Mitigations (22%)
| # | Objective | الزاوية OT | Phase / Lab | Status |
|---|---|---|---|---|
| 2.1 | Threat actors & motivations | nation-state ضد الشبكات (Sandworm/Ukraine) | P5 | ⬜ |
| 2.2 | Threat vectors & attack surfaces | USB، remote access للـ vendor، laptops المهندسين | P2 / P4 | ⬜ |
| 2.3 | Vulnerability types | default passwords، firmware قديم، بروتوكولات بلا auth | Lab 00 / P5 | ⬜ |
| 2.4 | Indicators of malicious activity | أوامر Modbus/104 غير متوقعة، GOOSE stNum غريب | P5 | ⬜ |
| 2.5 | Mitigation techniques (segmentation, hardening, least privilege…) | zones & conduits | P1 / P4 | ⬜ |

## Domain 3: Security Architecture (18%)
| # | Objective | الزاوية OT | Phase / Lab | Status |
|---|---|---|---|---|
| 3.1 | Architecture models (ICS/SCADA, cloud, IoT, segmentation) | Purdue model | P1 | ⬜ |
| 3.2 | Secure enterprise infrastructure (firewalls, IDS/IPS, jump server, VPN, 802.1X) | DMZ، jump server، firewall بين المستويات | P1 / P2 | ⬜ |
| 3.3 | Protecting data | configs و SCL files كبيانات حساسة | P4 | ⬜ |
| 3.4 | Resilience & recovery | PRP/HSR (تعرفها!)، backups، DR | P4 | ⬜ |

## Domain 4: Security Operations (28%) ← الأكبر
| # | Objective | الزاوية OT | Phase / Lab | Status |
|---|---|---|---|---|
| 4.1 | Secure baselines & hardening of computing resources | hardening للـ HMI و EWS و gateways | P4 | ⬜ |
| 4.2 | Asset management | asset inventory للمحطة (OT IDS يسويها) | P5 | ⬜ |
| 4.3 | Vulnerability management | patching في OT، CVEs للـ relays | P4 | ⬜ |
| 4.4 | Alerting & monitoring (SIEM, syslog, SNMP, NetFlow) | syslog من الـ switches للـ Wazuh | P3 | ⬜ |
| 4.5 | Enhance security (firewall rules, IDS/IPS, web filter, DNS, email, FIM) | قواعد firewall للـ 104/MMS | P1 / P3 | ⬜ |
| 4.6 | Identity & access management (AD, LDAP, RADIUS, SSO, MFA, PAM) | AD للمحطة، RADIUS للأجهزة، RBAC | P2 | ⬜ |
| 4.7 | Automation & orchestration | scripts لجمع configs و backups | P3 / P4 | ⬜ |
| 4.8 | Incident response | IR في OT: الأمان قبل الأدلة | P5 / P6 | ⬜ |
| 4.9 | Data sources for investigation | logs + pcaps + timeline | P3 | ⬜ |

## Domain 5: Security Program Management & Oversight (20%)
| # | Objective | الزاوية OT | Phase / Lab | Status |
|---|---|---|---|---|
| 5.1 | Security governance (policies, standards) | IEC 62443، NERC CIP | P6 | ⬜ |
| 5.2 | Risk management | risk assessment للمحطة | P6 | ⬜ |
| 5.3 | Third-party risk | الـ vendor remote access (GE نفسها!) | P6 | ⬜ |
| 5.4 | Compliance | متطلبات العميل في الـ specs | P6 | ⬜ |
| 5.5 | Audits & assessments, pentesting | Cyber FAT/SAT | P6 | ⬜ |
| 5.6 | Security awareness | تدريب مشغلي المحطة | P6 | ⬜ |

## Exam-only topics (ما لها لاب OT مباشر)
Cloud models، email security، web filtering، data sovereignty، بعض الـ crypto. نذاكرها بالقراءة والأسئلة.
