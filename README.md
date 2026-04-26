<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.1-red?style=for-the-badge&logo=github">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=opensourceinitiative">
  <img src="https://img.shields.io/badge/Made%20by-MRH-green?style=for-the-badge&logo=github">
</p>

<h1 align="center">🌍 MRH Universal Downloader</h1>
<h3 align="center">دانلود هر فایلی از هر سایتی - فقط با نوشتن یک کامیت مسیج</h3>
<h3 align="center">Download anything from anywhere - Just by writing a commit message</h3>

<p align="center">
  <b>✊ دسترسی به اطلاعات آزاد، یک حق بنیادین بشر است / Access to information is a human right</b>
</p>

---

## 💝 حمایت / Support

> اگر این ابزار به شما کمک کرد / If this tool helped you:

**BNB (BEP-20) - Ethereum - Arbitrum - Base:**  
`0x3A90B058E51deeA95dd8912b4bA71c4b159Ec582`

**USDT / USDC / DAI (BEP-20 / ERC-20 / Polygon):**  
`0x3A90B058E51deeA95dd8912b4bA71c4b159Ec582`

> *حمایت مالی کاملاً اختیاری است / Support is optional*

---

# 📖 راهنمای فارسی

## 🎯 این ابزار برای چه کسانی ساخته شده؟

| اگر در کشوری زندگی می‌کنید که... | این ابزار برای شماست |
|--------------------------------|---------------------|
| 🔴 یوتیوب مسدود است | ✅ دانلود ویدیو و موزیک |
| 🔴 اینستاگرام کار نمی‌کند | ✅ دانلود عکس و ویدیو |
| 🔴 نت ملی دسترسی به سایت‌ها را قطع کرده | ✅ دانلود از هر سایت |
| 🔴 نمی‌توانید نرم‌افزار دانلود کنید | ✅ دانلود نرم‌افزار و بازی |

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

### مرحله 4: اولین دانلود
1. هر فایلی را ویرایش کنید
2. در کامیت مسیج بنویسید:
3. dl: https://raw.githubusercontent.com/sample/test-file/main/sample.txt

4. 3. Commit کنید
4. بعد از ۱-۲ دقیقه، فایل در پوشه `downloads` ظاهر می‌شود

### مرحله 5: انتقال فایل به موبایل یا کامپیوتر
- **کامپیوتر:** روی فایل کلیک → Download
- **موبایل:** برنامه GitHub → باز کردن فایل → Download

## 📝 دستورات فارسی

| دستور | کاربرد | مثال |
|-------|--------|------|
| `dl: URL` | دانلود فایل | `dl: https://example.com/file.zip` |
| `dl-yt: URL` | دانلود یوتیوب | `dl-yt: https://youtu.be/VIDEO_ID` |
| `dl-yt: URL (mp3)` | دانلود صدای یوتیوب | `dl-yt: https://youtu.be/ID (mp3)` |
| `dl-zip: URL1 URL2` | دانلود چند فایل به صورت زیپ | `dl-zip: https://example.com/1.jpg https://example.com/2.jpg` |
| `dl-gh: URL` | دانلود از گیت‌هاب | `dl-gh: https://github.com/user/repo/releases/download/v1/app.zip` |
| `dl-extract: URL.zip` | دانلود و اکسترکت خودکار | `dl-extract: https://example.com/archive.zip` |
| `dl-chunk: URL` | دانلود فایل بزرگ | `dl-chunk: https://example.com/bigfile.zip` |
| `dl-stop` | توقف اضطراری | `dl-stop` |

## 🛡️ قوانین فارسی

### ✅ مجاز:
- دانلود فیلم آموزشی برای یادگیری شخصی
- دانلود نرم‌افزارهای متن‌باز و رایگان
- بکاپ شخصی

### ❌ ممنوع:
- دانلود فیلم، موسیقی دارای حق نشر بدون اجازه
- دانلود بدافزار یا محتوای غیراخلاقی
- استخراج ارز دیجیتال (ماینینگ)
- استفاده برای دور زدن تحریم‌های تجاری

## ❓ سوالات متداول فارسی

**س: رایگان است؟**  
ج: بله، ۱۰۰٪ رایگان

**س: محدودیت حجم؟**  
ج: حداکثر ۲۰ گیگ در هر اجرا

**س: هر چند وقت فورک را حذف کنم؟**  
ج: هر ۲-۳ ماه یا وقتی پوشه `downloads` پر شد

---

# 📖 English Guide

## 🎯 Who is this for?

| If you live in a country where... | This tool is for you |
|----------------------------------|---------------------|
| 🔴 YouTube is blocked | ✅ Download videos & music |
| 🔴 Instagram doesn't work | ✅ Download photos & videos |
| 🔴 Internet is heavily censored | ✅ Download from any site |
| 🔴 Can't download software | ✅ Download apps & games |

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

### Step 4: First Download
1. Edit any file
2. In commit message write:

3. dl: https://raw.githubusercontent.com/sample/test-file/main/sample.txt

4. 3. Commit changes
4. After 1-2 minutes, check the `downloads` folder

### Step 5: Transfer File to Your Device
- **Computer:** Click file → Download
- **Mobile:** GitHub app → Open file → Download

## 📝 Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `dl: URL` | Download file | `dl: https://example.com/file.zip` |
| `dl-yt: URL` | Download YouTube | `dl-yt: https://youtu.be/VIDEO_ID` |
| `dl-yt: URL (mp3)` | Download YouTube audio | `dl-yt: https://youtu.be/ID (mp3)` |
| `dl-zip: URL1 URL2` | Download multiple files as ZIP | `dl-zip: https://example.com/1.jpg https://example.com/2.jpg` |
| `dl-gh: URL` | Download from GitHub | `dl-gh: https://github.com/user/repo/releases/download/v1/app.zip` |
| `dl-extract: URL.zip` | Download and auto-extract | `dl-extract: https://example.com/archive.zip` |
| `dl-chunk: URL` | Download large files | `dl-chunk: https://example.com/bigfile.zip` |
| `dl-stop` | Emergency stop | `dl-stop` |

## 🛡️ Rules

### ✅ Allowed:
- Educational videos for personal learning
- Open-source and free software
- Personal backups

### ❌ Forbidden:
- Copyrighted movies, music, software without permission
- Malware or illegal content
- Cryptocurrency mining
- Bypassing trade sanctions

## ❓ FAQ

**Q: Is this free?**  
A: Yes, 100% free

**Q: File size limit?**  
A: Max 20GB per run

**Q: How often to refresh fork?**  
A: Every 2-3 months or when `downloads` folder is full

---

## 📜 مجوز / License

MIT License - Free to use, copy, modify, distribute with credit to MRH.

---

<p align="center">
<b>MRH Universal Downloader v1.0.1</b><br>
<b>ساخته شده با ❤️ برای آزادی اینترنت / Made with ❤️ for internet freedom</b>
</p>

<p align="center">
<a href="README.FA.md">📄 مشاهده راهنمای فارسی جداگانه</a> |
<a href="README.en.md">📄 View Separate English Guide</a>
</p>
</details>
