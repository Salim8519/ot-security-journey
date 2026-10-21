# OT Security Journey 🛡️⚡

**من مهندس SCADA/SAS إلى OT Security Engineer**
From SCADA / Substation Automation engineer to OT Security engineer.

هذا الـ repo هو المرجع الوحيد لكل شي: الخطة، اللابات، الأدوات، التقدم، المراجعات، والبورتفوليو.

---

## الهدف | Goal

- **الوظيفة المستهدفة:** OT Security Engineer في شركة متخصصة (Dragos, Claroty, Nozomi Networks, أو استشارات OT).
- **الشهادات:** CompTIA Security+ ← ISA/IEC 62443 Cybersecurity Fundamentals Specialist ← GICSP.
- **الميزة التنافسية:** خبرة حقيقية في IEC 61850 و DNP3 و IEC 104 و Modbus داخل محطات GE Vernova.

## المسارين بالتوازي | Two tracks, one system

| Security+ (النظرية) | OT Lab (التطبيق) |
|---|---|
| تقرأ عن المفهوم | تطبقه على محطة افتراضية |
| أسئلة بأسلوب الامتحان + PBQs | write-up موثق في `labs/` |

كل مفهوم في Security+ مربوط بلاب OT في [`secplus/objectives.md`](secplus/objectives.md).

## هيكل الـ repo | Structure

```
├── PROFILE.md            ملفي: خلفيتي، نقاط قوتي وضعفي
├── CLAUDE.md             تعليمات Claude لإدارة الجلسات والمتابعة
├── ROADMAP.md            المراحل الست ومعايير الانتقال
├── progress/
│   ├── TRACKER.md        لوحة التقدم (المرحلة الحالية، النسب، الخطوة الجاية)
│   └── sessions-log.md   سجل كل جلسة
├── secplus/
│   ├── objectives.md     أهداف Security+ مربوطة باللابات
│   └── notes/            ملاحظاتي لكل domain
├── labs/                 كل لاب في مجلد: README + scripts + captures
├── tools/                جرد الأدوات وطريقة تثبيتها + سكربتات مساعدة
├── review/
│   ├── question-bank.md  بنك أسئلة (Security+ و OT)
│   ├── weak-areas.md     نقاط الضعف اللي نرجع لها
│   └── weekly/           المراجعات الأسبوعية
└── templates/            قوالب الجلسة واللاب والمراجعة
```

## كيف تمشي الجلسة | Session flow (~45 min)

1. **Learn (10m):** مفهوم واحد من Security+.
2. **Lab (25m):** نطبقه في simulation أو على اللاب.
3. **Recall (10m):** أسئلة بأسلوب الامتحان.
4. **Log:** تحديث `progress/` و `review/` وcommit.

**أسبوع ضغط شغل:** 15 دقيقة أسئلة من الجوال فقط.
**أسبوع فاضي:** جلسات lab كاملة.

## الحالة الحالية | Current status

راجع [`progress/TRACKER.md`](progress/TRACKER.md).
