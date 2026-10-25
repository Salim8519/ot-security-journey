# Question Bank | بنك الأسئلة

> كل سؤال عليه: الـ objective، مرات الإجابة الصحيحة/الخاطئة. الأسئلة اللي تغلط فيها ترجع لك أكثر.
> Format: `[obj] [✔ n / ✘ n]`

---

### Q001 · [1.2] · [✔0 / ✘0]
في محطة كهرباء، أي ركن من أركان CIA عادةً له الأولوية الأعلى؟
A) Confidentiality  B) Integrity  C) Availability  D) Non-repudiation
<details><summary>الجواب</summary>

**C) Availability.** انقطاع التحكم أو الحماية ممكن يسبب انقطاع كهرباء أو خطر على الناس. لهذا في OT الترتيب غالباً A ← I ← C، عكس الـ IT. (Integrity قريبة جداً: أمر trip مزوّر خطير مثل الانقطاع.)
</details>

### Q002 · [2.3] · [✔0 / ✘0]
مهاجم على نفس الـ VLAN يرسل Modbus *Write Single Coil* لـ RTU ويفتح breaker. أي ثغرة استغلها بالأساس؟
A) Buffer overflow  B) Lack of authentication in the protocol  C) SQL injection  D) Weak encryption
<details><summary>الجواب</summary>

**B.** Modbus/TCP ما فيه أي authentication. أي جهاز يقدر يوصل port 502 يقدر يكتب. الحل: segmentation + firewall/DPI يسمح بـ function codes معينة من IPs معينة.
</details>

### Q003 · [1.1] · [✔0 / ✘0]
قفل على باب غرفة الـ control في المحطة، ما نوع الـ control؟
A) Technical, detective  B) Physical, preventive  C) Managerial, corrective  D) Operational, deterrent
<details><summary>الجواب</summary>

**B) Physical, preventive.** (كاميرا CCTV = physical, detective. لافتة "ممنوع الدخول" = deterrent.)
</details>

### Q004 · [3.1] · [✔0 / ✘0]
في Purdue model، وين المكان الطبيعي للـ historian اللي يحتاج يوصله مستخدمين من شبكة الشركة؟
A) Level 1  B) Level 2  C) Level 3.5 (IT/OT DMZ)  D) Level 0
<details><summary>الجواب</summary>

**C) DMZ.** مستخدمو الـ IT يوصلون نسخة الـ historian في الـ DMZ، وما في اتصال مباشر من IT لداخل الـ OT.
</details>

### Q005 · [4.6] · [✔0 / ✘0]
تبغى المهندسين يدخلون للـ switches والـ firewalls بحساباتهم الشخصية بدل حساب `admin` مشترك، مع تسجيل مين سوى وش. أي حل أنسب؟
A) Local accounts on each device  B) RADIUS/TACACS+ backed by AD  C) SNMPv1  D) Shared password vault only
<details><summary>الجواب</summary>

**B.** مصادقة مركزية + accounting. TACACS+ يفصل authorization لكل أمر وأفضل للأجهزة الشبكية، RADIUS أشهر وأبسط.
</details>

### Q006 · [4.4] · [✔0 / ✘0]
ليش الـ time synchronization (NTP/PTP) مهم أمنياً وليس تشغيلياً فقط؟
<details><summary>الجواب</summary>

لأن التحقيق في الحوادث يعتمد على ترتيب الأحداث من مصادر مختلفة (firewall، switch، HMI، relay). إذا الساعات مختلفة ما تقدر تبني timeline صحيح. وكمان شهادات TLS و Kerberos (AD) تعتمد على الوقت.
</details>

### Q007 · [4.1] · [✔0 / ✘0]
ليش application whitelisting غالباً أنسب من antivirus تقليدي على HMI في محطة؟
<details><summary>الجواب</summary>

الـ HMI يشغّل مجموعة برامج ثابتة لا تتغير تقريباً، فسهل تحدد المسموح وتمنع الباقي. الـ AV يحتاج تحديث signatures مستمر (صعب في شبكة معزولة)، وممكن يسبب false positive يوقف برنامج حرج أو يستهلك موارد.
</details>

### Q008 · [2.4] · [✔0 / ✘0]
في capture للـ GOOSE، لاحظت رسائل من نفس الـ goCB لكن `stNum` قفز من 15 لـ 9000 فجأة، وبعدها trip. وش تشك فيه؟
<details><summary>الجواب</summary>

**GOOSE spoofing / injection.** المهاجم يرسل stNum أعلى عشان الـ subscribers يقبلون رسالته كحدث جديد. هذا indicator لهجوم. الحماية: IEC 62351-6 (توقيع GOOSE)، segmentation، ومراقبة بـ OT IDS.
</details>

### Q009 · [5.3] · [✔0 / ✘0]
الـ vendor يحتاج remote access دائم لمحطة العميل للدعم. وش أفضل ممارسة؟
<details><summary>الجواب</summary>

لا اتصال دائم. الوصول عبر jump server في الـ DMZ، بـ MFA، يتفعّل عند الطلب ولمدة محددة (just-in-time)، مع تسجيل الجلسة (session recording) وموافقة المشغل.
</details>

### Q010 · [3.4] · [✔0 / ✘0]
وش الفرق بين PRP و RSTP من ناحية الـ availability؟
<details><summary>الجواب</summary>

RSTP يعيد بناء المسار بعد العطل (convergence بعشرات/مئات الـ ms). PRP يرسل كل frame على شبكتين مستقلتين بنفس الوقت، فالعطل ما يسبب أي فقد (zero recovery time). هذا مثال على resilience في Security+ 3.4.
</details>

### Q011 · [3.1] · [✔0 / ✘0]
تبغى VM تطلع للإنترنت، بس ما تبغى أي جهاز من شبكة البيت يقدر يوصلها. أي نوع شبكة في VMware؟
A) Bridged  B) NAT  C) Host-only  D) Custom بدون كرت
<details><summary>الجواب</summary>

**B) NAT.** الـ VM تطلع باسم جهازك، ومن برا ما يشوفونها. Bridged تخليها مكشوفة للكل، وHost-only ما فيها إنترنت أصلاً.
</details>

### Q012 · [2.5] · [✔0 / ✘0]
لابتوب مهندس مربوط بكابل على شبكة المحطة، وبنفس الوقت على WiFi الشركة. وش اسم هالمشكلة، وليش خطيرة؟
<details><summary>الجواب</summary>

**Dual-homed host.** اللابتوب يصير جسر بين الشبكتين ويتخطى الـ firewall. لو انخترق من جهة الـ IT، المهاجم يوصل للمحطة مباشرة. عشان كذا شلنا الـ host adapter من VMnet3.
</details>

### Q013 · [3.2] · [✔0 / ✘0]
ركبت firewall جديد بين IT وOT، وما كتبت ولا قاعدة على interface الـ OT. جهاز في الـ OT يحاول يوصل للإنترنت. وش يصير وليش؟
<details><summary>الجواب</summary>

**ينرفض.** الـ firewall يشتغل بمبدأ **default deny (implicit deny)**: أي ترافيك ما له قاعدة تسمح فيه صراحة ينرفض. شفناها في اللاب لما Debian طلع "Bad archive mirror".
</details>

### Q014 · [5.5 / 4.5] · [✔0 / ✘0]
وقت الـ commissioning فتح المهندس قاعدة "allow any" مؤقتة عشان يحمّل تحديثات، وبعد سنة القاعدة لين الحين موجودة. وش اسم المشكلة؟ وكيف تمنعها؟
<details><summary>الجواب</summary>

**Rule creep / stale temporary rules.** نمنعها بإن نسمي القاعدة بوضوح (TEMP + سبب + تاريخ انتهاء)، ونسوي firewall rule review دوري، وchange management. وفي الـ Cyber SAT نتأكد إن ما بقت ولا قاعدة any/any.
</details>

### Q015 · [3.1] · [✔0 / ✘0]
في IEC 62443، وش الفرق بين الـ **zone** والـ **conduit**؟ وطبقها على اللاب.
<details><summary>الجواب</summary>

**Zone** = مجموعة أصول لها نفس متطلبات الأمان (اللاب: IT zone وOT zone). **Conduit** = قناة الاتصال المتحكم فيها بين الـ zones (اللاب: الـ firewall OPNsense). أي اتصال بين zones لازم يمر عبر conduit معرّف.
</details>
