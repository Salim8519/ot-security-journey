# Mission 01: بناء شبكة المحطة | Build the substation network

> **Security+:** 3.1 (architecture / segmentation), 3.2 (firewalls), 2.5 (mitigation) · **IEC 62443:** zones & conduits, SR 5.1 · **XP:** 100

## الهدف
نبني شبكتين منفصلتين: IT وOT، وبينهم firewall. نتأكد إن أي اتصال من IT لـ OT لازم يمر على الـ firewall.

## التصميم
```
[Host PC = IT] ── VMnet2 10.10.10.0/24 ──┐
                                 [OPNsense] ── VMnet3 10.20.20.0/24 ── [Debian RTU]
                                      └── VMnet8 NAT (WAN، إنترنت)
```

| الجهاز | الكرت | IP |
|---|---|---|
| OPNsense `OTLAB-FW-OPNsense` | em0 = WAN (VMnet8 NAT) | DHCP: 192.168.98.137 |
| OPNsense | em1 = LAN، الاسم **IT** (VMnet2) | 10.10.10.254/24 |
| OPNsense | em2 = OPT1، الاسم **OT** (VMnet3) | 10.20.20.254/24 |
| Debian `OTLAB-RTU-Debian` (hostname `rtu01`) | ens33 على VMnet3 | 10.20.20.10/24، الـ GW والـ DNS: 10.20.20.254 |
| Host PC | VMware Network Adapter VMnet2 | 10.10.10.1 |
| Windows 10 x64 (IT workstation) | كرت 2 على VMnet2 | 10.10.10.50 (لاحقاً) |

مكان الـ VMs: `D:\Virtualizations\OTLAB\`

## Firewall rules (الحالة الحالية)
| Interface | Source | Destination | Action | الوصف |
|---|---|---|---|---|
| IT | IT net | any | Pass | Default allow LAN to any (افتراضية، **بنقيّدها**) |
| IT | IT net (v6) | any | Pass | Default allow LAN IPv6 (افتراضية) |
| OT | OT net | any | Pass | ⚠️ **TEMP - internet for setup, DELETE after** |
| (ضمني) | - | - | Block | default deny لأي شي ما له قاعدة |

## الخطوات
- [x] VMnet2 وVMnet3 في Virtual Network Editor (سواها سالم بيده لأن النافذة تحتاج admin)
- [x] فك ملف OPNsense من `.bz2` إلى `.iso`
- [x] VM حق OPNsense: 2GB RAM، 2 cores، 20GB، و3 كروت (NAT / VMnet2 / VMnet3)
- [x] تثبيت OPNsense على الـ disk (UFS)
- [x] إعادة توزيع الـ interfaces: WAN=em0، LAN=em1، OPT1=em2
- [x] الـ IPs: LAN 10.10.10.254، OPT1 10.20.20.254
- [x] دخول واجهة الويب على https://10.10.10.254 (الـ wizard انلغى، عادي)
- [x] تسمية الـ interfaces: LAN ← **IT**، OPT1 ← **OT**
- [x] VM حق Debian: 1GB RAM، 1 CPU، 10GB، وكرت واحد على VMnet3
- [x] تثبيت Debian: الشبكة يدوي، hostname، user `salim`، root فاضي (sudo)، تقسيم الـ disk
- [x] اكتشفنا إن الـ OT ما توصل للإنترنت ← **default deny يشتغل** ← أضفنا قاعدة TEMP
- [ ] 🟨 **إحنا هنا:** تثبيت Debian يكمّل من الـ mirror (deb.debian.org) ← Software selection: SSH + standard utilities بس
- [ ] بعد التثبيت: فصل الـ ISO، تصحيح الـ timezone (`sudo timedatectl set-timezone Asia/Muscat`)
- [ ] تثبيت Python + pymodbus، وتشغيل `rtu_sim.py`
- [ ] الاختبار 1: من IT نقرأ ونغير حالة الـ breaker (ينجح لأن قاعدة IT any)
- [ ] قواعد الحماية: نقيّد IT ← OT (Modbus 502 من IP معيّن بس) ونحذف قاعدة TEMP
- [ ] الاختبار 2: نجرب مرة ثانية ونتأكد إن الـ firewall منعه وسجّله في الـ log
- [ ] كرت ثاني لـ Windows 10 x64 على VMnet2

## مشاكل واجهتنا وحلولها
| المشكلة | السبب | الحل |
|---|---|---|
| ما قدرت (Claude) أعدّل في Virtual Network Editor | النافذة admin، وWindows UIPI يمنع التحكم فيها | سالم يسويها بيده |
| الكتابة ما توصل لشاشة الـ VM | VMware يقرأ الكيبورد الحقيقي بس | سالم يكتب في الـ consoles، وClaude يجهّز الـ VMs ويشتغل من واجهة الويب |
| OPNsense وزّع الكروت بالعكس | الـ auto-detect حط LAN على em0 (NAT) | Console ← option 1 ← يدوي |
| الأرقام في Debian installer | الوضع النصي يبغى **رقم** مو `yes` | اكتب الرقم |
| **Bad archive mirror** | الـ firewall مطفي، والـ OT ما لها قاعدة (default deny) | شغّل الـ firewall + قاعدة TEMP + **Apply** |
| القاعدة ما اشتغلت بعد Save | OPNsense يحفظ بالـ Save ويفعّل بالـ Apply بس | اضغط Apply دايماً |
| المتصفح المدمج يطلب موافقة على كل خطوة | 10.x عنوان خاص، والتطبيق يعتبره high-risk | الضبط اليدوي أسرع |

## مفاهيم تعلمناها في الطريق
- **Bridged / NAT / Host-only / DHCP:** [`secplus/notes/networking-basics.md`](../../secplus/notes/networking-basics.md)
- **Dual-homed host:** جهاز على شبكتين بنفس الوقت ويتخطى الـ firewall. عشان كذا شلنا الـ host adapter من VMnet3.
- **Default deny:** أي ترافيك ما له قاعدة تسمح فيه ينرفض. شفناه بعيننا لما الـ RTU ما قدر يحمّل.
- **Rule creep:** القواعد المؤقتة اللي تنسى تنحذف. عشان كذا سمينا القاعدة TEMP.
- **Anti-spoofing:** "Block private networks" على الـ WAN.
- **Zones & conduits (IEC 62443):** IT وOT zones، والـ firewall هو الـ conduit الوحيد بينهم.
