<p align="center">   
  <img src="https://img.shields.io/badge/Version-1.0.2-red?style=for-the-badge&logo=github">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=opensourceinitiative">
  <img src="https://img.shields.io/badge/Made%20by-MRH-green?style=for-the-badge&logo=github">
</p>

<h1 align="center">🌍 MRH Universal Downloader</h1>
<h3 align="center">دانلود از اینستاگرام، گیت‌هاب و هر سایت دیگر - فقط با نوشتن یک کامیت مسیج</h3>
<h3 align="center">Download from Instagram, GitHub and any site - Just by writing a commit message</h3>

<p align="center">
  <b>✊ دسترسی به اطلاعات آزاد، یک حق بنیادین بشر است / Access to information is a human right</b>
</p>

---

## 💝 حمایت / Support

> اگر این ابزار به شما کمک کرد / If this tool helped you:

**BNB (BEP-20) - Ethereum - Arbitrum - Base:*
`0x3A90B058E51deeA95dd8912b4bA71c4b159Ec582`

**USDT / USDC / DAI (BEP-20 / ERC-20 / Polygon):**  
`0x3A90B058E51deeA95dd8912b4bA71c4b159Ec582`

> *حمایت مالی کاملاً اختیاری است / Support is optional*

---

# 📖 راهنمای فارسی

## 🎯 این ابزار برای چه کسانی ساخته شده؟

| اگر در کشوری زندگی می‌کنید که... | این ابزار برای شماست |
|--------------------------------|---------------------|
| 🔴 اینستاگرام کار نمی‌کند | ✅ دانلود عکس، ویدیو و ریلز |
| 🔴 نمی‌توانید نرم‌افزار دانلود کنید | ✅ دانلود از گیت‌هاب |
| 🔴 نت ملی دسترسی به سایت‌ها را قطع کرده | ✅ دانلود از هر سایت با لینک مستقیم |

## ⚙️ این ابزار چطور کار می‌کند؟

1. شما یک لینک را در کامیت مسیج گیت‌هاب می‌نویسید
2. سرور گیت‌هاب (در کشور آزاد) درخواست دانلود می‌فرستد
3. فایل در مخزن شما ذخیره می‌شود
4. شما فایل را از گیت‌هاب دانلود می‌کنید

**🔑 بدون VPN، بدون پروکسی، فقط گیت‌هاب رایگان**

## 📝 راهنمای قدم به قدم

### مرحله 1: ساخت حساب گیت‌هاب
به `github.com` بروید و **Sign up** کنید (رایگان)

### مرحله 2: فورک کردن پروژه
روی دکمه **Fork** در بالا کلیک کنید

### مرحله 3: فعال کردن دسترسی نوشتن
به **Settings → Actions → General → Workflow permissions** بروید و **Read and write permissions** را انتخاب کنید

### مرحله 4: اولین دانلود تست
1. هر فایلی را در ریپو ویرایش کنید (مثلاً `README.md`)
2. در کامیت مسیج بنویسید:
dl: https://raw.githubusercontent.com/sample/test-file/main/sample.txt

3. روی **Commit changes** کلیک کنید
4. بعد از ۱-۲ دقیقه، به برگه **Code** بروید
5. پوشه `downloads/direct/` را باز کنید
6. ✅ فایل `sample.txt` را آنجا می‌بینید

### مرحله 5: انتقال فایل به موبایل یا کامپیوتر
- **کامپیوتر:** روی فایل کلیک → Download
- **موبایل:** برنامه GitHub → باز کردن فایل → Download

---

## 📝 دستورات کاربردی (تضمین شده)

| دستور | کاربرد | مثال |
|-------|--------|------|
| `dl-ig: URL` | دانلود از اینستاگرام (پست، ریلز، عکس) | `dl-ig: https://www.instagram.com/reel/xxxxx` |
| `dl-gh: URL` | دانلود از گیت‌هاب (ریلیزها) | `dl-gh: https://github.com/user/repo/releases/download/v1/file.zip` |
| `dl: URL1 URL2` | دانلود مستقیم از هر سایت (موزیک، ویدیو، عکس، نرم‌افزار) | `dl: https://example.com/music.mp3 https://example.com/photo.jpg` |
| `dl-stop` | توقف اضطراری دانلود | `dl-stop` |

---

## 🛡️ قوانین استفاده

### ✅ مجاز:
- دانلود محتوای عمومی اینستاگرام
- دانلود نرم‌افزارهای متن‌باز از گیت‌هاب
- دانلود فایل‌های عمومی از هر سایت

### ❌ ممنوع:
- دانلود محتوای دارای حق نشر بدون اجازه
- دانلود بدافزار یا محتوای غیراخلاقی
- استخراج ارز دیجیتال (ماینینگ)

### ⚠️ توجه:
- اینستاگرام محدودیت درخواست دارد. در صورت خطا، چند ساعت بعد دوباره امتحان کنید.
- فایل‌های بالای ۲۰ گیگابایت ممکن است با محدودیت گیت‌هاب مواجه شوند.

---

## ❓ سوالات متداول

**س: آیا این ابزار رایگان است؟**  
ج: بله، ۱۰۰٪ رایگان. فقط یک حساب گیت‌هاب نیاز دارید.

**س: چرا یوتیوب پشتیبانی نمی‌شود؟**  
ج: محدودیت فنی در سرورهای گیت‌هاب. در صورت رفع مشکل، اضافه خواهد شد.

**س: هر چند وقت باید فورک را حذف کنم؟**  
ج: هر ۲-۳ ماه یا وقتی پوشه `downloads` پر شد.

**س: چطور بفهمم دانلود تمام شده؟**  
ج: به تب `Actions` بروید. علامت سبز ✅ یعنی دانلود کامل شده است.

---

# 📖 English Guide

## 🎯 Who is this for?

| If you live in a country where... | This tool is for you |
|----------------------------------|---------------------|
| 🔴 Instagram doesn't work | ✅ Download photos, videos, reels |
| 🔴 Can't download software | ✅ Download from GitHub releases |
| 🔴 Internet is heavily censored | ✅ Download from any site with direct link |

## ⚙️ How it works

1. You write a link in a commit message on GitHub
2. GitHub servers (in free countries) request the file
3. The file is saved in your repository
4. You download the file from GitHub to your device

**🔑 No VPN, no proxy, just a free GitHub account**

## 📝 Step-by-Step Guide

### Step 1: Create GitHub Account
Go to `github.com` and click **Sign up** (free)

### Step 2: Fork this Repository
Click the **Fork** button at the top right

### Step 3: Enable Write Permissions
Go to **Settings → Actions → General → Workflow permissions** → Select **Read and write permissions** → Save

### Step 4: First Test Download
1. Edit any file in your repo (e.g., `README.md`)
2. In commit message write:

dl: https://raw.githubusercontent.com/sample/test-file/main/sample.txt

3. Click **Commit changes**
4. After 1-2 minutes, go to **Code** tab
5. Open `downloads/direct/` folder
6. ✅ You'll see `sample.txt` there

### Step 5: Transfer File to Your Device
- **Computer:** Click file → Download
- **Mobile:** GitHub app → Open file → Download

---

## 📝 Working Commands (Guaranteed)

| Command | Purpose | Example |
|---------|---------|---------|
| `dl-ig: URL` | Download from Instagram (post, reel, photo) | `dl-ig: https://www.instagram.com/reel/xxxxx` |
| `dl-gh: URL` | Download from GitHub releases | `dl-gh: https://github.com/user/repo/releases/download/v1/file.zip` |
| `dl: URL1 URL2` | Direct download from any site | `dl: https://example.com/music.mp3 https://example.com/photo.jpg` |
| `dl-stop` | Emergency stop | `dl-stop` |

---

## 🛡️ Rules

### ✅ Allowed:
- Download public Instagram content
- Download open-source software from GitHub
- Download public files from any site

### ❌ Forbidden:
- Copyrighted content without permission
- Malware or illegal content
- Cryptocurrency mining

### ⚠️ Note:
- Instagram has rate limits. If it fails, try again after a few hours.
- Files larger than 20GB may hit GitHub limits.

---

## ❓ FAQ

**Q: Is this free?**  
A: Yes, 100% free. Only a GitHub account needed.

**Q: Why no YouTube support?**  
A: Technical limitation on GitHub servers. Will be added if resolved.

**Q: How often to refresh fork?**  
A: Every 2-3 months or when `downloads` folder is full.

**Q: How to know download is complete?**  
A: Check `Actions` tab. Green checkmark ✅ means done.

---

## 📜 مجوز / License

MIT License - Free to use, copy, modify, distribute with credit to MRH.

---

<p align="center">
<b>MRH Universal Downloader v1.0.2</b><br>
<b>ساخته شده با ❤️ برای آزادی اینترنت / Made with ❤️ for internet freedom</b>
</p>

<p align="center">
<a href="README.FA.md">📄 مشاهده راهنمای فارسی جداگانه</a> |
<a href="README.en.md">📄 View Separate English Guide</a>
</p>
