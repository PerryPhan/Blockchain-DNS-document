import socket

# Khai báo CONST cần thiết config socket cho Client
HEADER = 64
PORT = 5050 # PORT của Server
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "11.0.0.254" # IP của Server
ADDR = (SERVER, PORT)

# Config Client kết nối ở IP và PORT đã chỉ định
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Hàm gửi message cho Connected Server
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

# Thực thi
send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")
# Thông thường client sau khi kết thúc sẽ disconnect
# và có lúc client muốn connect lại thì sẽ gặp vấn đề already connect 
# nên để tránh trường hợp trên, sẽ gửi trả cho Server để biết đang disconnect 
# TODO: Tìm hiểu vấn đề này sâu hơn
send(DISCONNECT_MESSAGE)