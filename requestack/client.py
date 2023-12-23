import socket

def send_request():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)

    try:
        client_socket.connect(server_address)
        message = "안녕하세요"
        client_socket.sendall(message.encode('utf-8'))

        data = client_socket.recv(1024).decode('utf-8')
        print("서버 응답:", data)
    finally:
        client_socket.close()

if __name__ == "__main__":
    send_request()
