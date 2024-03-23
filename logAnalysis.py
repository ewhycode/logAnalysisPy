import re

def analyzeLogs(log_file):
    suspicious_patterns = [
        r'(?i)password\s*=\s*[\'"].*?[\'"]',  #detect password leakage
        r'(?i)user\s*=\s*[\'"].*?[\'"]',      #detect username leakage
        r'(?i)access\s*denied',               #detect failed login attempts
        r'(?i)failed\s*password\s*for',      #detect failed login attempts
        r'(?i)(sql|code)\s*injection',       #detect SQL or code injection attempts
    ]

    with open(log_file, 'r') as f:
        for line_num, line in enumerate(f, start=1):
            for pattern in suspicious_patterns:
                if re.search(pattern, line):
                    print(f"Suspicious activity detected in line {line_num}:")
                    print(line.strip())
                    print("-" * 50)

#example usage
#if __name__ == "__main__":
 #   log_file = "path/to/your/log/file.log"
  #  analyzeLogs(log_file)
