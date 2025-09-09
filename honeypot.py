import socket
import paramiko
import threading
import logging

# Configure logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Dummy credentials to catch attackers
VALID_USERS = ["root", "admin"]
VALID_PASSWORDS = ["123456", "toor", "password"]

class SSHHoneypot(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        logging.info(f"Login attempt - USER: {username}, PASS: {password}")
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'

def handle_connection(client_socket, addr):
    transport = paramiko.Transport(client_socket)
    try:
        transport.add_server_key(paramiko.RSAKey.generate(2048))
        server = SSHHoneypot()
        transport.start_server(server=server)
    except Exception as e:
        logging.error(f"Error with {addr}: {e}")

    transport.close()

def main():
    host = "0.0.0.0"
    port = 2222  # Use non-standard port to avoid conflicts

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(100)

    print(f"[+] Honeypot listening on {host}:{port}")

    while True:
        client, addr = sock.accept()
        logging.info(f"Incoming connection from {addr[0]}")
        threading.Thread(target=handle_connection, args=(client, addr[0])).start()

if __name__ == "__main__":
    main()
