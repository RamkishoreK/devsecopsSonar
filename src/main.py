import os
import logging

# ❌ Hard-coded secret (Sonar will flag this)
API_KEY = "12345-SECRET-API-KEY"

# ❌ Logging configuration exposing sensitive info
logging.basicConfig(level=logging.DEBUG)


def insecure_calculate(expression):
    # ❌ Using eval() directly — Code Injection Vulnerability
    logging.debug(f"Evaluating: {expression}")  # ❌ Sensitive info in logs
    try:
        return eval(expression)  # Vulnerable
    except Exception as e:
        # ❌ Bad practice: printing internal error details
        print("Error occurred:", e)
        return None


def save_result_to_file(result):
    # ❌ No validation, writes arbitrary data
    with open("results.txt", "a") as f:
        f.write(str(result) + "\n")


def insecure_menu():
    print("=== Vulnerable Calculator ===")
    print("Enter any Python expression to evaluate")
    print("Example: 2+3 or __import__('os').system('rm -rf /')")

    # ❌ No input sanitization
    user_input = input("Enter expression: ")

    result = insecure_calculate(user_input)

    if result is not None:
        print("Result:", result)
        save_result_to_file(result)  # ❌ Writes untrusted data to file
    else:
        print("Calculation failed")


if __name__ == "__main__":
    # ❌ Debug mode intentionally enabled
    print("API Key in use:", API_KEY)
    insecure_menu()
