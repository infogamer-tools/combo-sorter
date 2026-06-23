# 🧹 Combo Sorter – Clean Combos & Xbox Codes Instantly

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

A lightweight GUI tool that sorts messy text logs and instantly extracts:
- **Cleaned account combos** (`email:pass` or `user:pass`)  
- **Xbox / Microsoft 25‑character codes** (XXXXX-XXXXX-XXXXX-XXXXX-XXXXX)

Perfect for security researchers, data cleaners, and anyone dealing with unformatted credential dumps (for authorised use only).

> **Made by [info.gamer](https://github.com/infogamer-tools)**  
> 🔗 **Repo:** [https://github.com/infogamer-tools/combo-sorter](https://github.com/infogamer-tools/combo-sorter)  
> 💬 **Discord:** [https://discord.gg/wXW43zf352](https://discord.gg/wXW43zf352) – Join for support & updates!

---

## ✨ Features

- 📋 **Paste & Extract** – Drop your messy text and get clean results in one click.
- 📁 **File Loader** – Open `.txt` files directly (UTF‑8).
- 🔐 **Combo Cleaner** – Isolates the first valid `user:pass` chunk from each line, skipping garbage.
- 🎮 **Xbox Code Grabber** – Finds all 5‑group codes (case‑insensitive, outputs uppercase).
- 🖥️ **Zero Dependencies** – Only uses Python standard library (`tkinter`, `re`).
- ⚡ **Instant Results** – Works in milliseconds.

---

## 📦 Requirements

- Python **3.8+** (no extra packages needed)

```bash
# Just run the script
python combo_sorter.py
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/infogamer-tools/combo-sorter.git
cd combo-sorter

# 2. Run the app
python combo_sorter.py
```

The GUI window will open. From there:
- **Paste** your messy text into the top box, or  
- **Click "📁 Open File"** to load a `.txt` file.
- **Click "🧹 Clean Accounts"** to extract only valid `user:pass` combos.
- **Click "🎮 Extract Xbox Codes"** to find and uppercase all 5‑group codes.
- **Click "🗑️ Clear Both"** to reset the fields.

---

## 🧠 How It Works

### Combo Cleaning
For each line, the tool grabs the first “word” (split by space), then splits again by `|`.  
If that chunk contains `:` and is longer than 5 characters, it’s treated as a valid combo.  
This filters out timestamps, log noise, and usernames without passwords.

### Xbox Code Extraction
Uses a regex matching the standard Microsoft 25‑character code pattern:
```
\b[A-Za-z0-9]{5}-[A-Za-z0-9]{5}-[A-Za-z0-9]{5}-[A-Za-z0-9]{5}-[A-Za-z0-9]{5}\b
```
All found codes are converted to uppercase for uniform output.

---

## 📚 Use Cases

- Cleaning and sorting leaked credential lists (authorised research only)
- Extracting game codes from chat logs or giveaway lists
- Pre-processing messy text exports for further tools
- Educational demonstrations of regex and Tkinter

---

## ⚠️ Important Disclaimer

**This tool is strictly for educational and ethical purposes.**

- Do **not** use it to process, distribute, or access unauthorised accounts.
- You are solely responsible for complying with all applicable laws and platform terms.
- The author (**info.gamer / infogamer-tools**) assumes no liability for misuse.

**Modification & redistribution** are allowed only if:
- You do **not** use the tool for unauthorised or unethical activities.
- You retain proper credit to the original author.
- Any repost includes the same usage restrictions.

---

## 🤝 Contributing

Pull requests are welcome!  
Possible improvements:
- Additional extraction patterns (Steam keys, URLs, emails)
- Export results to file
- Drag‑and‑drop support
- Dark mode toggle

Ensure contributions stay educational and ethical.

---

## 📜 License

MIT – see [LICENSE](LICENSE) for details.  
© 2026 [info.gamer](https://github.com/infogamer-tools)

---

## ⭐ Support

If this tool helps you, drop a ⭐ on GitHub and join the community:

- **Discord:** [https://discord.gg/wXW43zf352](https://discord.gg/wXW43zf352)  
- **GitHub:** [https://github.com/infogamer-tools/combo-sorter](https://github.com/infogamer-tools/combo-sorter)
