import base64
import argparse
import string
import re
import os
from datetime import datetime
from argon2.low_level import hash_secret_raw, Type

TOOL_NAME = "Encpass"
AUTHOR = "Shariful Islam"
VERSION = "1.0"

def banner():
    print(f"\n🔒 {TOOL_NAME} - Deterministic Password Generator")
    print(f"👑 Author: {AUTHOR}")
    print(f"🚀 Version: {VERSION}\n")

def generate_password(master_password, account_name, length=16):
    if length < 8 or length > 16:
        raise ValueError("Password length must be between 8 and 16")

    combined = (master_password + ":" + account_name).encode('utf-8')
    salt = b"MyFixedDeterministicSalt"

    hash_bytes = hash_secret_raw(
        secret=combined,
        salt=salt,
        time_cost=2,
        memory_cost=65536,
        parallelism=2,
        hash_len=32,
        type=Type.ID
    )

    b64 = base64.urlsafe_b64encode(hash_bytes).decode('utf-8')
    b64 = b64.replace('=', '').replace('-', '').replace('_', '')

    if length <= 10:
        num_specials = 1
    elif length <= 12:
        num_specials = 3
    else:
        num_specials = 4

    specials = "!@#$%^&*()-_=+[]{};:,.<>?"
    special_chars = ""
    for i in range(num_specials):
        index = hash_bytes[i] % len(specials)
        special_chars += specials[index]

    upper = next((c for c in b64 if c in string.ascii_uppercase), 'A')
    lower = next((c for c in b64 if c in string.ascii_lowercase), 'a')
    digit = next((c for c in b64 if c in string.digits), '9')

    core = upper + lower + digit + special_chars
    needed = length - len(core)
    core += b64[:needed]

    return core[:length]

def process_file(input_file, length):
    output_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        number_match = re.match(r"\s*(\d+)", line)
        if not number_match:
            continue
        number = number_match.group(1)

        quotes = re.findall(r'"([^"]+)"', line)
        if len(quotes) < 2:
            continue

        master = quotes[0]
        account = quotes[1]

        password = generate_password(master, account, length)
        output_lines.append(f"{number}. {password}")
    return output_lines

def ensure_passwords_dir():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pass_dir = os.path.join(script_dir, "passwords")
    os.makedirs(pass_dir, exist_ok=True)
    return pass_dir

def get_datetime_filename():
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S") + ".txt"

def main():
    banner()

    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} - Secure password generator tool")
    parser.add_argument("-m", "--master", help="Master password")
    parser.add_argument("-a", "--account", help="Account identifier")
    parser.add_argument("-f", "--file", help="Input file for bulk password generation")
    parser.add_argument("-o", "--output", help="Output file path (optional)")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length (8-16, default 16)")

    args = parser.parse_args()

    if args.file:
        results = process_file(args.file, args.length)
        for r in results:
            print(r)

        if args.output:
            out_path = args.output
            if not os.path.isabs(out_path):
                out_path = os.path.join(os.getcwd(), out_path)
        else:
            pass_dir = ensure_passwords_dir()
            input_basename = os.path.basename(args.file)
            input_name, _ = os.path.splitext(input_basename)
            out_path = os.path.join(pass_dir, f"{input_name}_output.txt")

        with open(out_path, 'w', encoding='utf-8') as f_out:
            for r in results:
                f_out.write(r + "\n")
        print(f"\n✅ All passwords saved to {out_path}\n")

    elif args.master and args.account:
        password = generate_password(args.master, args.account, args.length)
        print(f"\nGenerated password for {args.account}: {password}\n")

        if args.output:
            out_path = args.output
            if not os.path.isabs(out_path):
                out_path = os.path.join(os.getcwd(), out_path)
        else:
            pass_dir = ensure_passwords_dir()
            filename = get_datetime_filename()
            out_path = os.path.join(pass_dir, filename)

        with open(out_path, 'w', encoding='utf-8') as f_out:
            f_out.write(password + "\n")
        print(f"✅ Password saved to {out_path}\n")

    else:
        print("❗ Please provide either -m + -a for single password OR -f for file bulk mode.")

if __name__ == "__main__":
    main()
