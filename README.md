# Honeypot Server to Detect Attack Patterns

A lightweight SSH honeypot written in Python that logs malicious login attempts, parses attacker data, and visualizes geolocation of intrusions.

---

## 📦 Features

- Custom SSH honeypot using `paramiko`
- Logs IP, attempted usernames, passwords
- Parses logs to detect frequent offenders
- Visualizes attacker IPs on a world map
- Integrates with `fail2ban` to block malicious IPs (optional)

---

## 🛠 Requirements
pip install -r requirements.txt

## How to Run
Start Honeypot
sudo python3 honeypot.py
(Default port: 2222 — open it in firewall settings)

View Logs
cat honeypot.log

Analyze Logs
python3 log_parser.py

Visualize Attack Map
python3 visualize_attackers.py
Opens attack_map.html with red markers for attacker IPs.

🛡️ Optional: Block IPs Using fail2ban
Install fail2ban:
sudo apt install fail2ban

Configure jail:
[honeypot]
enabled = true
filter = honeypot
port = 2222
logpath = /path/to/honeypot.log
maxretry = 5
bantime = 600

Create filter file /etc/fail2ban/filter.d/honeypot.conf:
[Definition]
failregex = .*Incoming connection from <HOST>

Restart fail2ban:
sudo systemctl restart fail2ban

📊 Sample Output
Incoming connection from 192.168.1.45
Login attempt - USER: root, PASS: admin

🌐 Attack Map Preview
(Add this after running the tool)

📁 Deliverables
✅ honeypot.py - the SSH trap
✅ honeypot.log - attacker logs
✅ log_parser.py - analytics
✅ visualize_attackers.py - map generation
✅ README.md - documentation
