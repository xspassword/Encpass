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
👉 Required package: `argon2-cffi`  

pip install argon2-cffi

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

Copyright (c) 2025 Shariful Islam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
