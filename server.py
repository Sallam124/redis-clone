# server.py
import socket
import threading
from datastore import DataStore  

# Create a single shared instance of DataStore
store = DataStore()

# Server settings
HOST = '127.0.0.1'  # Localhost
PORT = 6379         # Default Redis port

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"[+] Redis clone server started on {HOST}:{PORT}")

# Function to handle each client in its own thread
def handle_client(client_socket, addr):
    print(f"[+] Connection from {addr}")
    client_socket.sendall("Welcome to Sallam's Redis 👋\n> ".encode())

    with client_socket:
        while True:
            try:
                data = client_socket.recv(1024).decode().strip()
                if not data:
                    break

                parts = data.split()
                if not parts:
                    client_socket.sendall(b"Invalid command\n> ")
                    continue

                cmd = parts[0].upper()

                if cmd == "SET" and len(parts) == 3:
                    key, value = parts[1], parts[2]
                    result = store.set(key, value)
                    client_socket.sendall(f"{result}\n> ".encode())

                elif cmd == "GET" and len(parts) == 2:
                    key = parts[1]
                    result = store.get(key)
                    client_socket.sendall(f"{result}\n> ".encode())

                elif cmd == "DEL" and len(parts) == 2:
                    key = parts[1]
                    result = store.delete(key)
                    client_socket.sendall(f"Deleted: {result}\n> ".encode())

                elif cmd == "EXISTS" and len(parts) == 2:
                    key = parts[1]
                    result = store.exists(key)
                    client_socket.sendall(f"{result}\n> ".encode())

                elif cmd == "INCR" and len(parts) == 2:
                    key = parts[1]
                    result = store.incr(key)
                    client_socket.sendall(f"{result}\n> ".encode())

                else:
                    client_socket.sendall(b"Unknown or invalid command\n> ")

            except ConnectionResetError:
                print(f"[-] Client {addr} disconnected unexpectedly.")
                break

# Main server loop that accepts multiple clients
while True:
    client_socket, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()
