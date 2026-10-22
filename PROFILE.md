# Learner Profile | ملف المتعلم

> آخر تحديث: 2026-10-21. يتحدث كل ما تغيّر شي.

## الوضع الحالي
- **الوظيفة:** SCADA Engineer, GE Vernova Grid Automation، يشتغل على SAS (Substation Automation Systems).
- **الهدف:** التحول لوظيفة OT Security في شركة متخصصة (Dragos / Claroty / Nozomi / استشارات).
- **اللغة المفضلة:** عربي (لهجة خليجية) + المصطلحات التقنية بالإنجليزي.

## الخبرة

| المجال | المستوى | ملاحظات |
|---|---|---|
| IEC 61850 (MMS, GOOSE) | ✅ عملي | شغله اليومي |
| DNP3 / IEC 104 / Modbus | ✅ عملي | |
| Redundancy (RSTP/PRP/HSR) | ✅ عملي | اشتغل عليه بنفسه |
| Wireshark | 🟡 يستخدمه | |
| Linux CLI | 🟡 يستخدمه | |
| Scripting (Python/PowerShell) | 🟡 بمساعدة AI | الهدف: يفهم ويعدّل ويشرح الكود بنفسه |
| Managed switches (GE S20) | 👀 شاهد | زملاؤه ضبطوها |
| Firewalls (Fortinet VMs) | 👀 شاهد | |
| Active Directory / LDAP / RADIUS / RBAC | 👀 شاهد | فكرة بسيطة |
| Syslog / Aggregator / SIEM / OT IDS / NTP | 📖 معرفة نظرية | |
| Antivirus / Whitelisting / Patching / Hardening / Backup | 👀 شاهد | ما يعرفها بعمق |
| Purdue model / DMZ / Jump server | 👀 شاهد في الـ field | |
| Security fundamentals | 🔴 مبتدئ | |

**الخلاصة:** يعرف *وش* المكونات، ناقصه *يضبطها بيده* ويفهم *ليش* تنضبط بهالطريقة.

## الموارد المتاحة
- **الجهاز:** لابتوب Windows قوي يشغل VMs. التفاصيل في قسم "الجهاز واللاب" تحت.
- **أجهزة حقيقية:** تقريباً مرتين بالسنة. نجهز لها checklist مسبقاً.
- **فريق Cyber منفصل في GE** يسوي Cyber FAT/SAT. فرصة للحضور والتعلم.
- **الوقت:** متغير. أحياناً ضغط شغل وأحياناً فاضي.
- **الميزانية:** تعلّم ذاتي مع Claude (simulations, computer use, browser).

## الجهاز واللاب (آخر فحص: 2026-10-22)
| البند | القيمة |
|---|---|
| Host | لابتوب Windows (`desktop-bq6ecr7`)، x64، كرت شبكة Realtek Gaming GbE، كرت NVIDIA |
| RAM / CPU / Disk | ❓ ما تأكدنا. الـ VM حق Win10 GPG ماخذ 8GB و4 cores، فالجهاز غالباً 16GB أو أكثر |
| Hypervisor | **VMware Workstation Pro 17** |
| مكان الـ VMs | `D:\Virtualizations\` |
| ISOs | في `Downloads`: OPNsense 26.7 وDebian 13.7 netinst |

**الـ VMs الموجودة من قبل** (نستفيد منها في المراحل الجاية):
| VM | الاستخدام في الخطة |
|---|---|
| Windows 10 x64 | ✅ **جهاز IT في اللاب** (نضيف له كرت على VMnet2) |
| Windows 10 x64 GPG | شخصي، **لا نلمسه** |
| Windows 11 x64 | |
| WS2019_DC1 / WS2019_DC2 | Phase 2: Active Directory |
| WSUS WS2019 | Phase 4: patch management |
| Windows Server 2019 | Jump server أو RADIUS (NPS) |
| kali-linux-2024.4 | attacker / أدوات |
| GNS3 | محاكاة switches في Phase 1 |

**الشبكات الافتراضية:**
| VMnet | النوع | Subnet | الدور |
|---|---|---|---|
| VMnet0 | Bridged | - | موجودة من قبل |
| VMnet1 | Host-only | 192.168.92.0/24 | موجودة من قبل |
| VMnet8 | NAT | 192.168.98.0/24 | موجودة من قبل، تُستخدم WAN للـ firewall |
| VMnet2 | Host-only, no DHCP | 10.10.10.0/24 | **IT zone** (Mission 01) |
| VMnet3 | Host-only, no DHCP, **بدون host adapter** | 10.20.20.0/24 | **OT zone** (Mission 01) |

**ملاحظة لـ Claude:** نافذة Virtual Network Editor تشتغل كـ admin، وWindows (UIPI) يمنع computer use من التحكم فيها. أي تعديل على الشبكات يسويه سالم بيده.

## أسلوب التعلم المناسب
- **يتعلم بالممارسة: يركّب ويشغّل.** ما يقرأ كتب، وما يحب التحليل العميق (يخليه للـ AI).
- كل جلسة = مهمة فيها شي يركّبه، والفهم يجي خفيف من خلال التركيب.
- الشرح لازم يكون بالعربي البسيط ومع أمثلة من الحياة.
- يحب نظام النقاط والمهمات (XP، رتب، Boss fights).
- جلسات قصيرة مرنة بدل جدول أسبوعي ثابت.
- ربط كل مفهوم بشي يعرفه من المحطة.
