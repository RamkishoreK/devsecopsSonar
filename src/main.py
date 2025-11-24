"""
-------------------------------------------------------------
WARNING: This file is intentionally vulnerable.
It exists ONLY for testing SonarQube / SonarCloud SAST tools.
DO NOT use in any real application.
-------------------------------------------------------------
"""

import os
import sqlite3
import subprocess
import hashlib
import random


# -------------------------------------------------------------
# Hardcoded secret (S2068)
# -------------------------------------------------------------
API_KEY = "12345-very-insecure-api-key"   # Sonar should flag this


# -------------------------------------------------------------
# SQL Injection (S3649)
# -------------------------------------------------------------
def get_user_password(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # ❌ Vulnerable: direct string concatenation
    query = f"SELECT password FROM users WHERE username = '{username}';"
    print("Executing SQL:", query)

    cur.execute(query)  # Sonar should flag this
    result = cur.fetchone()
    conn.close()
    return result


# -------------------------------------------------------------
# Command Injection (S4721)
# -------------------------------------------------------------
def run_ping(host):
    # ❌ Vulnerable: user-controlled shell command
    cmd = "ping -c 1 " + host
    return subprocess.check_output(cmd, shell=True)  # Sonar should flag


# -------------------------------------------------------------
# Insecure eval (S2076 / S5334)
# -------------------------------------------------------------
def calc_user_expression(expr):
    # ❌ Vulnerable: runs arbitrary Python
    return eval(expr)


# -------------------------------------------------------------
# Path Traversal (S2083)
# -------------------------------------------------------------
def read_any_file(filename):
    # ❌ No validation
    with open(filename, "r") as f:
        return f.read()


# -------------------------------------------------------------
# Weak hashing (S4790)
# -------------------------------------------------------------
def weak_hash(data):
    # ❌ Weak MD5 hash
    return hashlib.md5(data.encode()).hexdigest()


# -------------------------------------------------------------
# Predictable random (S2245)
# -------------------------------------------------------------
def insecure_token():
    # ❌ Not cryptographically secure
    return str(random.randint(100000, 999999))


# -------------------------------------------------------------
# MAIN (for demonstration)
# -------------------------------------------------------------
if __name__ == "__main__":
    print("=== Vulnerable Python File for Sonar Testing ===")

    print(get_user_password("example.db", "admin' OR '1'='1"))
    print(run_ping("127.0.0.1"))
    print(calc_user_expression("2 + 5"))
    print(read_any_file("/etc/passwd"))
    print(weak_hash("password"))
    print(insecure_token())
