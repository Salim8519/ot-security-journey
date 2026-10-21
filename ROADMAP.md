# Roadmap | خارطة الطريق

الفكرة: نبني **محطة افتراضية مؤمّنة** على اللابتوب، طبقة طبقة. كل مرحلة تغطي جزء من Security+ وتضيف طبقة أمنية للاب.

```
Phase 0  الأساسيات          ──► Security+ D1 + networking
Phase 1  الشبكة             ──► D3 (architecture)
Phase 2  الهوية والصلاحيات  ──► D4.6 (IAM)
Phase 3  السجلات والمراقبة  ──► D4.4, 4.9
Phase 4  الـ Endpoints       ──► D4.1-4.3, 2.5
Phase 5  البروتوكولات والكشف ──► D2 (threats, indicators)
Phase 6  المعايير والبورتفوليو ──► D5 + IEC 62443
```

---

## Phase 0: Foundations | الأساسيات
**Security+:** Domain 1 (General Security Concepts) + أساسيات الشبكات
- CIA triad (ولليش الـ OT يقلبها: Availability أولاً)، أنواع الـ controls، AAA
- TCP/IP بعمق، ports، subnetting، ARP
- Wireshark: فلترة، follow stream، تحليل Modbus/GOOSE
- Linux CLI أساسي
**Labs:** 00 Modbus without authentication، 01 Wireshark على ترافيك محطة
**✅ تنتقل لما:** تشرح ليش Modbus/GOOSE ما فيها authentication، وتحلل capture بنفسك.

## Phase 1: Network Security | الشبكة
**Security+:** 3.1, 3.2
- Purdue model، zones & conduits
- VLANs، port security، segmentation (S20-style switch concepts)
- Firewall: قواعد، default deny، NAT، stateful (pfSense / FortiGate VM)
- IT/OT DMZ
**Lab:** بناء شبكة محطة على مستويات Purdue في VMs + firewall بين المستويات
**✅ تنتقل لما:** ترسم وتبني DMZ وتبرر كل قاعدة firewall.

## Phase 2: Identity & Access | الهوية والصلاحيات
**Security+:** 4.6, 1.2
- Windows Server + Active Directory + GPOs
- LDAP vs RADIUS vs TACACS+، و RBAC على IEDs (IEC 62351-8)
- MFA، least privilege، jump server للـ remote access
**Lab:** دومين للمحطة، HMI و EWS على الدومين، RADIUS لمصادقة الـ switch/firewall
**✅ تنتقل لما:** مهندس "وهمي" يدخل للمحطة عن طريق jump server فقط ومسجّل.

## Phase 3: Logging & Monitoring | السجلات والمراقبة
**Security+:** 4.4, 4.9
- Syslog، log aggregation، SIEM (Wazuh)
- NTP/PTP وليش الوقت مهم للتحقيق
- SPAN/TAP، passive monitoring
**Lab:** كل الأجهزة ترسل لـ Wazuh، ونكتب alerts لدخول فاشل وتغيير config
**✅ تنتقل لما:** تحقق في حادثة وهمية من السجلات وتبني timeline.

## Phase 4: Endpoint Security | حماية الأجهزة
**Security+:** 4.1, 4.2, 4.3, 2.5
- Antivirus vs application whitelisting (ليش الـ whitelisting أنسب للـ OT)
- Hardening: services، USB، GPOs، CIS benchmarks
- Patch management في OT (ليش ما نقدر نحدّث بأي وقت)
- Backup & recovery للـ configs
**Lab:** hardening لـ HMI VM + whitelisting + خطة backup
**✅ تنتقل لما:** تسوي hardening checklist وتطبقها وتقيس الفرق.

## Phase 5: OT Protocols, Attacks & Detection | البروتوكولات والهجمات والكشف
**Security+:** Domain 2
- هجمات على Modbus، DNP3، IEC 104، GOOSE spoofing، MMS
- IEC 62351 كحل
- Zeek + ICS parsers، Suricata، Security Onion
- تحليل Industroyer / Industroyer2 وهجمات أوكرانيا
**Lab:** نهاجم IEDs وهمية ونكشف الهجوم
**✅ تنتقل لما:** تكتب detection rule لهجوم سويته بنفسك.

## Phase 6: Standards & Portfolio | المعايير والبورتفوليو
**Security+:** Domain 5
- IEC 62443 (3-3 SRs، security levels، 2-4)، NIST SP 800-82
- Risk assessment، Cyber FAT/SAT
**Lab:** تسوي Cyber FAT كامل على اللاب مقابل IEC 62443-3-3
**✅ النهاية:** repo عام بالـ write-ups + Security+ + جاهز لـ ISA 62443 و GICSP.

---

## الشهادات | Certifications
1. **CompTIA Security+** (نقرر 701 أو 801 بعد Phase 1، حسب السرعة)
   - SY0-801 متوقع نوفمبر 2026، و SY0-701 متوقع يتقاعد منتصف 2027. نتأكد من موقع CompTIA قبل الحجز.
2. **ISA/IEC 62443 Cybersecurity Fundamentals Specialist**
3. **GICSP** (GIAC)

## خارج الـ repo
- اطلب من فريق Cyber في GE تحضر Cyber FAT/SAT الجاي.
- جهّز checklist لكل مرة توصل فيها لأجهزة حقيقية (`labs/real-hardware-checklist.md`).
