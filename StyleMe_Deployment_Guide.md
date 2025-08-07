# دليل نشر تطبيق StyleMe على GitHub و Vercel

**المؤلف:** Manus AI  
**الإصدار:** 1.0.0  
**التاريخ:** 31 يوليو 2025

## مقدمة

يهدف هذا الدليل إلى توفير إرشادات شاملة خطوة بخطوة لنشر تطبيق StyleMe، الذي يتكون من واجهة أمامية مبنية باستخدام React وواجهة خلفية مبنية باستخدام Flask، على منصتي GitHub و Vercel. سيضمن هذا الدليل أن يكون مشروعك مهيأً بشكل صحيح للتحكم في الإصدار والنشر المستمر، مما يتيح لك عرض تطبيقك مباشرة بعد عملية الإعداد.

تُعد GitHub منصة أساسية لاستضافة الكود والتحكم في الإصدار، بينما تُقدم Vercel بيئة نشر قوية وسهلة الاستخدام، خاصة لتطبيقات الواجهة الأمامية (مثل React) مع دعم للوظائف بدون خادم (Serverless Functions) التي يمكن استخدامها للواجهة الخلفية (مثل Flask). باتباع هذا الدليل، ستتمكن من إعداد سير عمل نشر سلس لمشروعك.

## المتطلبات الأساسية

قبل البدء، تأكد من توفر المتطلبات التالية:

1.  **تطبيق StyleMe جاهز:** يجب أن يكون لديك مجلد مشروع StyleMe الكامل على جهازك المحلي. هذا المجلد هو `AIHaircutAppConcept` ويحتوي على كل من مجلدات الواجهة الأمامية (`workspace/shadcn-ui`) والواجهة الخلفية (`backend/backend_app`).
2.  **حساب GitHub:** ستحتاج إلى حساب GitHub لإنشاء مستودع واستضافة الكود الخاص بك. إذا لم يكن لديك حساب، يمكنك التسجيل مجانًا على [github.com](https://github.com/).
3.  **حساب Vercel:** ستحتاج إلى حساب Vercel لنشر تطبيقك. يمكنك التسجيل مجانًا على [vercel.com](https://vercel.com/).
4.  **تثبيت Git:** تأكد من تثبيت Git على نظامك. يمكنك تنزيله من [Git-SCM.com](https://git-scm.com/downloads).
5.  **فهم أساسيات سطر الأوامر:** سيتضمن هذا الدليل استخدام سطر الأوامر (Command Prompt أو PowerShell على Windows) لتنفيذ أوامر Git.
6.  **قاعدة بيانات خارجية (موصى بها للإنتاج):** نظرًا لأن Vercel هي منصة بدون خادم، فإنها لا تدعم قواعد البيانات المستمرة مثل SQLite مباشرة في بيئة الإنتاج. يوصى بشدة باستخدام قاعدة بيانات خارجية مثل PostgreSQL أو MySQL المستضافة على خدمة سحابية (مثل Render.com، ElephantSQL، Supabase، أو AWS RDS). ستحتاج إلى عنوان URL لاتصال قاعدة البيانات هذه.

## الجزء الأول: إعداد المشروع لـ GitHub

في هذا الجزء، سنقوم بتهيئة مستودع Git محلي، وإنشاء ملف `.gitignore` لاستبعاد الملفات غير الضرورية، ثم دفع المشروع إلى مستودع GitHub جديد.

### 1. تهيئة مستودع Git

افتح موجه الأوامر (Command Prompt) أو PowerShell وانتقل إلى المجلد الرئيسي لمشروع StyleMe. هذا هو المجلد الذي يحتوي على مجلد `AIHaircutAppConcept`.

```cmd
cd C:\Path\To\Your\StyleMe_Project\AIHaircutAppConcept
git init
```

**ملاحظة:** استبدل `C:\Path\To\Your\StyleMe_Project\AIHaircutAppConcept` بالمسار الفعلي لمجلد مشروعك.

### 2. إنشاء ملف `.gitignore`

لقد قمت بالفعل بإنشاء ملف `.gitignore` ووضعه في جذر مجلد `AIHaircutAppConcept`. هذا الملف يضمن أن الملفات غير الضرورية مثل `node_modules`، `venv`، وملفات `.env` الحساسة لن يتم رفعها إلى GitHub. محتوى الملف هو كالتالي:

```
# Node.js dependencies
node_modules/

# Python virtual environment
virtualenv/
virtualenvs/
vendored/
venc/
venv/

# Build artifacts
build/
dist/
*.egg-info/

# Logs and databases
*.log
*.sqlite3
*.db

# OS generated files
.DS_Store
thumbs.db

# Environment variables
.env
.env.*

# IDE specific files
.idea/
.vscode/
*.iml

# Uploads and temporary files
uploads/
*.zip
*.tar.gz
*.rar

# DeepFace models (can be large)
.deepface/

# Frontend specific build output
AIHaircutAppConcept/workspace/shadcn-ui/dist/

# Backend specific build output
AIHaircutAppConcept/backend/backend_app/instance/

# Vercel specific
.vercel/
```

### 3. إضافة الملفات إلى منطقة التجهيز (Staging Area)

الآن، أضف جميع ملفات مشروعك إلى منطقة التجهيز في Git. تأكد من أنك في المجلد الرئيسي لمشروع `AIHaircutAppConcept`.

```cmd
git add .
```

يمكنك التحقق من حالة المستودع الخاص بك باستخدام `git status`.

### 4. الالتزام بالتغييرات (Commit)

قم بإنشاء الالتزام الأولي الذي سيتضمن جميع ملفات مشروعك:

```cmd
git commit -m "Initial commit: Add StyleMe application files"
```

### 5. إنشاء مستودع GitHub جديد

1.  اذهب إلى [github.com](https://github.com/) وسجل الدخول.
2.  انقر على زر `+` في الزاوية العلوية اليمنى، ثم اختر `New repository`.
3.  املأ التفاصيل:
    *   **Repository name:** اختر اسمًا (مثال: `StyleMe-App`).
    *   **Description (اختياري):** أضف وصفًا.
    *   **Public أو Private:** اختر ما تفضله.
    *   **لا تقم بتهيئة المستودع بـ README أو .gitignore أو ترخيص.**
4.  انقر على `Create repository`.

### 6. ربط المستودع المحلي بالمستودع البعيد

بعد إنشاء المستودع على GitHub، ستنتقل إلى صفحة تعرض لك تعليمات. انسخ الأمر الذي يربط المستودع البعيد (عادةً ما يبدأ بـ `git remote add origin ...`) والصقه في موجه الأوامر الخاص بك:

```cmd
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
```

**ملاحظة:** استبدل `YOUR_USERNAME` باسم المستخدم الخاص بك و `YOUR_REPOSITORY_NAME` باسم المستودع الخاص بك.

### 7. دفع الكود إلى GitHub

ادفع الالتزامات المحلية الخاصة بك إلى مستودع GitHub البعيد:

```cmd
git push -u origin main
```

قد يطلب منك Git إدخال اسم المستخدم وكلمة المرور الخاصة بك على GitHub. إذا كنت تستخدم المصادقة الثنائية (2FA)، فستحتاج إلى استخدام رمز وصول شخصي (Personal Access Token - PAT) بدلاً من كلمة المرور.

تهانينا! لقد قمت برفع تطبيق StyleMe بنجاح إلى GitHub.

## الجزء الثاني: إعداد المشروع لـ Vercel

في هذا الجزء، سنقوم بإعداد ملف `vercel.json` الذي قمت بإنشائه مسبقًا، والذي يخبر Vercel بكيفية بناء ونشر تطبيقك متعدد الأجزاء (React و Flask).

### 1. وضع ملف `vercel.json`

لقد قمت بالفعل بإنشاء ملف `vercel.json` ووضعه في جذر مجلد `AIHaircutAppConcept`. هذا الملف هو كالتالي:

```json
{
  "version": 2,
  "name": "styleme-app",
  "builds": [
    {
      "src": "workspace/shadcn-ui/package.json",
      "use": "@vercel/node",
      "config": {
        "buildCommand": "npm install && npm run build",
        "outputDirectory": "dist"
      }
    },
    {
      "src": "backend/backend_app/src/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "backend/backend_app/src/main.py"
    },
    {
      "src": "/(.*)",
      "dest": "workspace/shadcn-ui/dist/$1"
    }
  ],
  "env": {
    "FLASK_ENV": "production",
    "SECRET_KEY": "@secret_key",
    "DATABASE_URL": "@database_url",
    "CORS_ORIGINS": "https://your-vercel-domain.vercel.app"
  },
  "functions": {
    "backend/backend_app/src/main.py": {
      "runtime": "python3.9"
    }
  }
}
```

### 2. فهم التكوين الرئيسي لـ `vercel.json`

*   **`builds`:** يخبر Vercel بكيفية بناء الواجهة الأمامية (React) والواجهة الخلفية (Flask).
    *   **الواجهة الأمامية:** يستخدم `@vercel/node` لبناء مشروع React الموجود في `workspace/shadcn-ui`. يقوم بتشغيل `npm install` ثم `npm run build`، ويضع المخرجات في مجلد `dist`.
    *   **الواجهة الخلفية:** يستخدم `@vercel/python` لبناء تطبيق Flask الموجود في `backend/backend_app/src/main.py`.
*   **`routes`:** يحدد كيفية توجيه الطلبات.
    *   أي طلب يبدأ بـ `/api/` يتم توجيهه إلى الواجهة الخلفية (Flask).
    *   جميع الطلبات الأخرى يتم توجيهها إلى الواجهة الأمامية (ملفات React المبنية).
*   **`env`:** يحدد متغيرات البيئة لتطبيقك على Vercel.
    *   `FLASK_ENV`: تم تعيينه على `production`.
    *   `SECRET_KEY` و `DATABASE_URL`: هذه هي متغيرات بيئة حساسة. **يجب عليك تعيين قيمها كمتغيرات بيئة سرية في إعدادات مشروع Vercel الخاص بك (Settings -> Environment Variables) بدلاً من وضعها مباشرة في `vercel.json` لأسباب أمنية.**
    *   `CORS_ORIGINS`: يجب تحديث هذا ليتضمن نطاق Vercel الخاص بك (مثال: `https://your-vercel-domain.vercel.app`) لتمكين طلبات CORS من الواجهة الأمامية إلى الواجهة الخلفية.
*   **`functions`:** يحدد بيئة تشغيل Python لوظيفة Flask بدون خادم (Serverless Function).

### 3. إعداد متغيرات البيئة في Vercel

هذه خطوة حاسمة لنجاح النشر. ستحتاج إلى إضافة متغيرات البيئة التالية إلى مشروعك على Vercel:

1.  **سجل الدخول إلى Vercel:** اذهب إلى [vercel.com](https://vercel.com/) وسجل الدخول إلى حسابك.
2.  **اختر مشروعك:** بعد ربط مستودع GitHub الخاص بك بـ Vercel (الخطوة التالية)، اختر مشروع StyleMe الخاص بك.
3.  **انتقل إلى الإعدادات:** اذهب إلى `Settings` -> `Environment Variables`.
4.  **أضف المتغيرات التالية:**
    *   **`SECRET_KEY`:** قم بإنشاء مفتاح سري قوي وفريد لتطبيق Flask الخاص بك. يمكنك استخدام مولد مفاتيح عشوائية عبر الإنترنت أو أمر Python مثل `python -c 'import os; print(os.urandom(24))'`.
    *   **`DATABASE_URL`:** عنوان URL لاتصال قاعدة بياناتك الخارجية (PostgreSQL، MySQL، إلخ). على سبيل المثال: `postgresql://user:password@host:port/database_name`.
    *   **`CORS_ORIGINS`:** هذا مهم لتمكين الواجهة الأمامية من الاتصال بالواجهة الخلفية. قم بتعيينها على النطاق الذي ستنشره Vercel عليه. بعد النشر الأول، يمكنك الحصول على هذا النطاق من إعدادات مشروع Vercel الخاص بك. على سبيل المثال: `https://styleme-app.vercel.app`.

**ملاحظة هامة:** تأكد من أن هذه المتغيرات `SECRET_KEY` و `DATABASE_URL` و `CORS_ORIGINS` تم تعيينها كـ **Secret Environment Variables** في Vercel.

## الجزء الثالث: النشر على Vercel

الآن بعد أن أصبح مشروعك على GitHub وملف `vercel.json` في مكانه الصحيح، يمكنك نشر تطبيقك على Vercel.

### 1. ربط مستودع GitHub بـ Vercel

1.  **سجل الدخول إلى Vercel:** اذهب إلى [vercel.com](https://vercel.com/) وسجل الدخول.
2.  **استيراد مشروع جديد:** في لوحة تحكم Vercel، انقر على `Add New...` ثم `Project`.
3.  **استيراد مستودع Git:** اختر `Import Git Repository` وحدد مستودع StyleMe الخاص بك من GitHub.
4.  **تكوين المشروع:**
    *   **Root Directory:** تأكد من أن الدليل الجذر للمشروع هو `AIHaircutAppConcept` (المجلد الذي يحتوي على `vercel.json`).
    *   **Build and Output Settings:** يجب أن يكتشف Vercel تلقائيًا إعدادات البناء من `vercel.json`. تأكد من أن الإعدادات تبدو صحيحة.
    *   **Environment Variables:** أضف متغيرات البيئة التي ذكرناها في الخطوة السابقة (`SECRET_KEY`, `DATABASE_URL`, `CORS_ORIGINS`).
5.  **انقر على `Deploy`:** سيبدأ Vercel عملية البناء والنشر. قد يستغرق هذا بعض الوقت، حيث سيقوم ببناء الواجهة الأمامية والخلفية.

### 2. مراقبة النشر

بعد النقر على `Deploy`، ستنتقل إلى صفحة سجلات النشر. راقب هذه السجلات عن كثب. إذا كانت هناك أي أخطاء في البناء أو النشر، فستظهر هنا. بمجرد اكتمال النشر بنجاح، ستوفر لك Vercel عنوان URL لتطبيقك المنشور.

### 3. التحقق من التطبيق المنشور

افتح عنوان URL الذي قدمته Vercel في متصفح الويب الخاص بك. يجب أن ترى الواجهة الأمامية لتطبيق StyleMe تعمل. اختبر وظائف الواجهة الأمامية والخلفية (مثل تسجيل الدخول، إنشاء تسريحة شعر، الحجز) للتأكد من أن كل شيء يعمل بشكل صحيح.

**ملاحظات هامة بعد النشر:**

*   **تحديث `CORS_ORIGINS`:** بعد النشر الأول، ستحصل على نطاق Vercel لتطبيقك (مثال: `https://styleme-app.vercel.app`). **عد إلى إعدادات مشروع Vercel الخاص بك وقم بتحديث متغير البيئة `CORS_ORIGINS` ليتضمن هذا النطاق المحدد.** هذا يضمن أن الواجهة الأمامية يمكنها الاتصال بالواجهة الخلفية بشكل صحيح.
*   **قاعدة البيانات:** تذكر أن قاعدة البيانات SQLite التي قد تكون استخدمتها محليًا لن تعمل على Vercel. تأكد من أن `DATABASE_URL` يشير إلى قاعدة بيانات خارجية تعمل بشكل صحيح.
*   **ملفات AI الكبيرة:** إذا واجهت مشكلات في نشر نماذج AI الكبيرة، فقد تحتاج إلى استضافة هذه النماذج بشكل منفصل أو استخدام خدمات AI خارجية توفر واجهات برمجة تطبيقات (APIs) للوصول إليها.

## استكشاف الأخطاء وإصلاحها

*   **فشل البناء (Build Failure):** تحقق من سجلات البناء في Vercel. قد تكون هناك أخطاء في الكود، أو تبعيات مفقودة، أو مشاكل في أوامر البناء في `vercel.json`.
*   **أخطاء وقت التشغيل (Runtime Errors):** إذا تم البناء بنجاح ولكن التطبيق لا يعمل، تحقق من سجلات وقت التشغيل في Vercel. قد تكون هناك مشكلات في الاتصال بقاعدة البيانات، أو متغيرات بيئة غير صحيحة، أو أخطاء في الكود الخلفي.
*   **مشاكل CORS:** إذا كانت الواجهة الأمامية لا تستطيع الاتصال بالواجهة الخلفية، فتأكد من أن `CORS_ORIGINS` في متغيرات بيئة Vercel يتضمن النطاق الدقيق لتطبيق Vercel الخاص بك.
*   **مشاكل `main` الفرع:** تأكد من أن الفرع الرئيسي في مستودع GitHub الخاص بك هو `main` (وليس `master` إذا كنت قد استخدمت هذا الاسم سابقًا). يمكن لـ Vercel تكوين النشر من أي فرع، ولكن `main` هو الافتراضي.

باتباع هذا الدليل، يجب أن تكون قادرًا على نشر تطبيق StyleMe بنجاح على Vercel، مما يجعله متاحًا للجمهور.

