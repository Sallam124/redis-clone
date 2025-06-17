import socket

HOST = '127.0.0.1'
PORT = 6379

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect to server. Make sure the server is running.")
        exit()

    print("Connected to Sallam's Redis CLI. Type commands like SET key value")

    welcome = s.recv(1024).decode()
    print(welcome.strip())

    while True:
        command = input("Sallam's-redis> ")
        if not command:
            continue
        if command.lower() == "exit":
            print("Goodbye!")
            break
        try:
            s.sendall(command.encode())
            response = s.recv(1024).decode()
            print(response.strip())
        except (ConnectionResetError, BrokenPipeError):
            print("Server disconnected.")
            break
