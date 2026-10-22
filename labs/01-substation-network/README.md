# Mission 01: بناء شبكة المحطة | Build the substation network

> **Security+:** 3.1 (architecture / segmentation), 2.5 (mitigation) · **IEC 62443:** zones & conduits, SR 5.1 · **XP:** 100

## الهدف
نبني شبكتين منفصلتين: IT وOT، وبينهم firewall. نتأكد إن أي اتصال من IT لـ OT لازم يمر على الـ firewall.

## التصميم
```
[Windows 10 x64 = IT] ── VMnet2 10.10.10.0/24 ──┐
                                        [OPNsense] ── VMnet3 10.20.20.0/24 ── [Debian RTU]
                                             └── VMnet8 NAT (WAN، إنترنت)
```

| الجهاز | الكرت | IP |
|---|---|---|
| OPNsense | WAN (VMnet8 NAT) | DHCP من VMware |
| OPNsense | LAN/IT (VMnet2) | 10.10.10.254/24 |
| OPNsense | OT (VMnet3) | 10.20.20.254/24 |
| Debian RTU | VMnet3 | 10.20.20.10/24، والـ gateway هو 10.20.20.254 |
| Windows 10 x64 (IT) | كرت 2 على VMnet2 | 10.10.10.50/24 |
| Host (جهازك) | VMware Network Adapter VMnet2 | 10.10.10.1 (VMware يعطيه تلقائي) |

## الخطوات
- [x] VMnet2 وVMnet3 في Virtual Network Editor (سواها سالم بيده لأن النافذة تحتاج admin)
- [ ] فك ملف OPNsense (`.bz2` ← `.iso`)
- [ ] VM حق OPNsense: 2GB RAM، و3 كروت شبكة
- [ ] تثبيت OPNsense + تحديد الـ interfaces والـ IPs
- [ ] VM حق Debian: 1GB RAM، وكرت واحد على VMnet3
- [ ] تثبيت Debian (بدون desktop) وIP ثابت
- [ ] كرت ثاني لـ Windows 10 x64 على VMnet2
- [ ] اختبار: ping من IT لـ OT **قبل** وبعد قواعد الـ firewall
- [ ] تشغيل `rtu_sim.py` على Debian، والوصول له من IT عبر الـ firewall

## مفاهيم تعلمناها في الطريق
- **Bridged / NAT / Host-only / DHCP:** راجع [`secplus/notes/networking-basics.md`](../../secplus/notes/networking-basics.md)
- **Dual-homed host:** جهاز مربوط على شبكتين بنفس الوقت ويتخطى الـ firewall. عشان كذا شلنا الـ host adapter من VMnet3.
