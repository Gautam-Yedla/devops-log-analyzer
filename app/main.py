import re

def analyze_log(file_path):
    errors, warnings = [], []
    with open(file_path, 'r') as file:
        for line in file:
            if "error" in line.lower():
                errors.append(line.strip())
            elif "warning" in line.lower():
                warnings.append(line.strip())
    return errors, warnings

if __name__ == "__main__":
    path = "sample_logs/app.log"
    errs, warns = analyze_log(path)
    print("\n⚠️ Warnings:\n", *warns, sep="\n")
    print("\n❌ Errors:\n", *errs, sep="\n")
