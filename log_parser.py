import re
from collections import Counter

def parse_log(log_file='honeypot.log'):
    with open(log_file, 'r') as f:
        lines = f.readlines()

    ips = []
    attempts = []

    for line in lines:
        if "Incoming connection" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ips.append(ip_match.group(1))
        elif "Login attempt" in line:
            attempts.append(line.strip())

    print(f"Unique IPs: {len(set(ips))}")
    print("Top 5 IPs:")
    for ip, count in Counter(ips).most_common(5):
        print(f"{ip}: {count} attempts")

    return list(set(ips))
