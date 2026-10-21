# Lab 00: Modbus Without Authentication

> **Security+:** 1.2 (CIA في OT), 2.3 (vulnerability types) · **OT angle:** IEC 62443-3-3 SR 1.1, SR 1.2 · **Difficulty:** ⭐

## الهدف
تفهم بشكل عملي ليش بروتوكولات OT القديمة (Modbus, DNP3, IEC 104) ما فيها authentication، وليش الحماية لازم تكون **حول** البروتوكول مو **داخله**.

## الخلفية
Modbus صُمّم في 1979 لشبكة serial معزولة. ما كان فيه مفهوم "مهاجم على الشبكة". لما انتقل لـ TCP/IP بقي كما هو: **أي جهاز يوصل port 502 يقدر يقرأ ويكتب بدون أي هوية**. نفس القصة مع DNP3 و IEC 104 الأساسيين — هذا ليش IEC 62351 و segmentation موجودين.

هذا بالضبط اللي تشوفه في المحطة: الـ RTU/gateway ما يسأل مين أنت، يعتمد كلياً على إن الشبكة "موثوقة".

## البيئة
كلها على `127.0.0.1` في بيئة التدريب — لا علاقة لها بأي جهاز حقيقي.

| الملف | الدور |
|---|---|
| `rtu_sim.py` | RTU وهمي يحاكي breaker + قياسات، Modbus/TCP على 5020 |
| `observe_client.py` | عميل قراءة فقط (مثل HMI أو OT monitoring tool) |

```bash
pip install --break-system-packages pymodbus
python rtu_sim.py          # terminal 1: شغّل المحطة
python observe_client.py   # terminal 2: اقرأ حالتها
```

## الخطوات
1. شغّل الـ RTU وراقب خط الحالة اللي يطبع breaker/current/voltage.
2. شغّل `observe_client.py`. **لاحظ: ما طلب منك أي user أو password.**
3. افتح Wireshark على الـ loopback وفلتر `modbus`. شوف الـ function codes بوضوح على الشبكة — بدون تشفير، بدون توقيع.

## النتائج
- الاتصال نجح بصفر credentials.
- الـ request/response واضح تماماً في Wireshark: function code، address، value. أي أحد يراقب الشبكة يقرأ حالة المحطة كاملة.
- نفس القناة اللي تقرأ بها، يُكتب بها (function codes مختلفة فقط). القراءة والكتابة ما بينهم فرق أمني في البروتوكول نفسه.

## الكشف | Detection
المدافع ما يقدر يعتمد على البروتوكول، فيراقب **السلوك**:
- **Baseline:** في محطة، مين عادةً يرسل write commands؟ غالباً الـ HMI/SCADA master فقط، من IP معروف.
- **Indicator:** write command من IP غير متوقع (laptop مهندس، جهاز غريب) = علامة إنذار.
- **Tools:** OT IDS (Nozomi/Claroty/Dragos) تبني baseline تلقائي وتنبّه على أي master جديد أو function code غير معتاد. بدونها: Zeek مع ICSNPP-Modbus parser (Phase 5).
- **Wireshark filter للتحقيق:** `modbus.func_code == 5 || modbus.func_code == 6 || modbus.func_code == 16` (الكتابة).

## الحماية | Mitigation (الأهم)
البروتوكول ما بيتغير، فالحماية طبقات حوله:
1. **Segmentation (IEC 62443 zones & conduits):** الـ RTU في zone محمية. لا أحد يوصل port 502 إلا عبر conduit معرّف.
2. **Firewall مع Modbus DPI:** يسمح فقط لـ master IP بإرسال write function codes؛ القراءة للباقي إذا لزم.
3. **Allowlist على مستوى الشبكة:** أي جهاز غير مصرح ما يوصل أصلاً.
4. **IEC 62351 / Secure variants:** حيث الأجهزة تدعم (DNP3-SA، TLS للـ MMS).
5. **Monitoring:** الكشف أعلاه — تفترض إن الوقاية ممكن تفشل.

ربط IEC 62443-3-3:
- **SR 1.1/1.2** (identification & authentication) — البروتوكول يفشل فيها، فنعوّضها بـ compensating controls.
- **SR 5.1** (network segmentation) — خط الدفاع الأساسي.
- **SR 6.2** (continuous monitoring) — الكشف.

## وش تعلمت
1. انعدام الـ authentication مو "bug" في الجهاز، هو خاصية البروتوكول التاريخية.
2. في OT، الـ **Availability** و **Integrity** أهم من Confidentiality: أمر مزوّر لفتح breaker أخطر من تسريب قراءة.
3. الحماية في OT = compensating controls حول البروتوكول، مو إصلاح البروتوكول.

## أسئلة مقابلة متوقعة
- "ليش ما نشفّر Modbus ببساطة؟" → التأخير (latency) والأجهزة القديمة والتوافق؛ ولهذا segmentation أولاً.
- "محطة فيها Modbus، كيف تأمّنها بدون تغيير الأجهزة؟" → zones/conduits، firewall DPI، allowlist، monitoring.
- "كيف تكشف write command خبيث؟" → baseline للـ masters الشرعيين + تنبيه على أي write من مصدر جديد.
