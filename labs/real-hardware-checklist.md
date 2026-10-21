# Real Hardware Checklist | قائمة الأجهزة الحقيقية

> تقريباً مرتين بالسنة توصل لأجهزة حقيقية. لا تضيع الفرصة. **فقط بإذن ومن غير ما تأثر على أي مشروع أو عميل.**

## قبل
- [ ] أخذت إذن واضح من المسؤول
- [ ] الأجهزة غير متصلة بأي شبكة إنتاج
- [ ] جهزت أسئلة لزميل يعرف الجهاز

## Switch (مثل GE S20)
- [ ] شفت VLANs و port security
- [ ] وين تنضبط الـ RADIUS / local users؟
- [ ] syslog و SNTP settings
- [ ] الـ services المفتوحة (HTTP/HTTPS/SSH/Telnet/SNMP version)
- [ ] backup للـ config ووين ينحفظ

## Firewall (Fortinet)
- [ ] قرأت الـ policies وفهمت كل قاعدة
- [ ] وش الـ zones / interfaces؟
- [ ] هل فيه DPI / application control لبروتوكولات OT؟
- [ ] logging لوين يروح؟

## Relay / Gateway
- [ ] الـ RBAC والأدوار الموجودة
- [ ] كيف تتغير الـ default passwords
- [ ] ports و services المفتوحة
- [ ] firmware version وفيه CVEs؟
- [ ] security event log في الجهاز

## بعد
- [ ] كتبت ملاحظات في `labs/` (بدون معلومات حساسة عن العميل)
