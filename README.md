# 🔒 Encpass

**Encpass** হলো একটি CLI ভিত্তিক deterministic password generator tool, যা নিরাপদ এবং জটিল password তৈরি করে।  
আপনি master password + account name ব্যবহার করে বারবার একই input দিলে একই secure password পাবেন।  
এটি single এবং bulk দুইভাবেই password তৈরি করতে পারে।  

---

## 🚀 Features
✅ Deterministic password generation (same input → same output)  
✅ Argon2 hashing + base64 + special char mix  
✅ Single mode 👉 output file name = date + time  
✅ Bulk mode 👉 output file name = input file name + `_output.txt`  
✅ Auto creates `passwords/` folder  
✅ No nested folders — clean structure  
✅ CLI banner with tool name, author, version  

---

## 📦 Requirements
👉 Python 3.6+  
👉 Required package: `argon2-cffi`  'pip install argon2-cffi'

---

## ⚡ Usage

### Single Mode
python3 password_tool.py -m YOUR_MASTER -a ACCOUNT_NAME

➡ Example output file: `passwords/20250705_235959.txt`

### Bulk Mode
python3 password_tool.py -f input_list.txt


➡ Example output file: `passwords/input_list_output.txt`

### Custom output file
python3 password_tool.py -m YOUR_MASTER -a ACCOUNT_NAME -o mypass.txt
python3 password_tool.py -f input_list.txt -o bulk_pass.txt


---

## 📄 Input file format (bulk mode)
Input file-এর প্রতিটি লাইনে এমন data থাকবে:
"MasterPass" "AccountName"

"MasterPass" "AnotherAccount"
...


👉 Tool প্রতিটি লাইনের প্রথম দুইটি double-quote এর ভেতরের string নিয়ে password তৈরি করবে।

---

## 👑 Author
Shariful Islam  

## 🏷 Version
1.0  

## 📜 License
MIT License
