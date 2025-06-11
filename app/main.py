# import os
# import re

# def analyze_log(file_path):
#     errors, warnings = [], []
#     with open(file_path, 'r') as file:
#         for line in file:
#             if "error" in line.lower():
#                 errors.append(line.strip())
#             elif "warning" in line.lower():
#                 warnings.append(line.strip())
#     return errors, warnings

# if __name__ == "__main__":
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     path = os.path.join(base_dir, "app", "sample_logs", "app.log")
#     errs, warns = analyze_log(path)
#     print("\n⚠️ Warnings:\n", *warns, sep="\n")
#     print("\n❌ Errors:\n", *errs, sep="\n")

import re
import os
try:
    from utils.email_alerts import send_email
except ImportError:
    from app.utils.email_alerts import send_email

from dotenv import load_dotenv

def analyze_log(file_path):
    errors, warnings = [], []
    with open(file_path, 'r') as file:
        for line in file:
            if "error" in line.lower():
                errors.append(line.strip())
            elif "warning" in line.lower():
                warnings.append(line.strip())
    return errors, warnings

def main(path="sample_logs/app.log"):
    load_dotenv()
    errs, warns = analyze_log(path)

    print("\n⚠️ Warnings:\n", *warns, sep="\n")
    print("\n❌ Errors:\n", *errs, sep="\n")

    subject = "Log Analysis Result"
    if errs:
        subject += " - Errors Found ❌"
    else:
        subject += " - No Errors ✅"

    body = f"Warnings:\n" + "\n".join(warns) + "\n\nErrors:\n" + "\n".join(errs)
    send_email(
        subject=subject,
        body=body,
        to_email=os.getenv("EMAIL_TO"),
        from_email=os.getenv("EMAIL_FROM"),
        password=os.getenv("EMAIL_PASS")
    )

    return errs, warns

if __name__ == "__main__":
    main()
