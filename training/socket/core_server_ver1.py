import socket
import threading

# Khai báo CONST cần thiết config socket cho Server
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# Config Server kết nối ở IP và PORT đã chỉ định 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Hàm xử lý thông tin từ tất cả Connected client 
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    # Mỗi khi client send 1 message bất kì sẽ có 2 gói tin [tự cho]
    # Gói tin #1 chứa số kí tự message 
    # Gói tin #2 chứa message
    connected = True
    while connected:
        # Gói tin #1
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            # Gói tin #2
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            # Gửi đi tin nhắn đã nhận
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

# Hàm thực thi "lắng nghe" các gói tin
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # Khởi tạo thread thực hiện công việc độc lập có khả năng cho kết nối nhiều client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Khi mở sẽ có 2 thread tính thêm cả Server
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()