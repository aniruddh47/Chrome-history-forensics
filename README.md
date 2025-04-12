A digital forensics project that extracts and analyzes Chrome browsing history using Python and SQLite. Includes both automation via script and manual analysis via SQLite GUI.
# 🔍 Chrome History Forensics Project

This is a mini **Digital Forensics** project to analyze Google Chrome browsing history using:

- ✅ Python script (for automated extraction)
- ✅ SQLite DB Browser (for manual inspection)

---

## 🎯 Objective

To extract and analyze the browser history stored in Chrome’s internal SQLite database and demonstrate two forensic approaches:
1. Python-based scripting (automated)
2. GUI-based analysis using DB Browser for SQLite

---

## 🛠 Tools Used

| Tool              | Purpose                                 |
|------------------|-----------------------------------------|
| **Python**        | Extract and convert history automatically |
| **SQLite Browser**| View and analyze data manually via GUI  |

---

## 🧪 Python Script: `main.py`

This script connects to the Chrome history SQLite database and extracts:
- Website URL
- Page Title
- Visit Count
- Last Visit Timestamp (converted to readable format)

### 📌 Steps to Run:

1. 🔒 **Close Chrome completely** (so the History file is not locked)
2. 📁 **Copy the History file** using this command in CMD:

🖥️ SQLite GUI Method (DB Browser)

For a manual approach using the GUI:
📌 Steps:

    Install SQlite in your system
     
    Open DB Browser for SQLite

    Click on "Open Database" → Select your copied History file
    mostly history file is stored in C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data\Default\History

    Go to Browse Data tab

    From the dropdown, choose table: urls

    You'll see columns like:

        url → Visited website

        title → Page title

        visit_count → Number of visits

        last_visit_time → Raw Chrome timestamp (optional manual conversion)
