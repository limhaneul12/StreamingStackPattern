import socket


def start_server() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    
    server_socket.listen(1)
    
    print("서버 시작 클라이언트 연결을 기다립니다")
    
    while True:
        connection, client_address = server_socket.accept()
        
        try:
            print("클라이언트 연결 완료", client_address)
            data = connection.recv(1024).decode("utf-8")
            if data:
                print("client request", data)
                response = "요청 확인"
                connection.sendall(response.encode("utf-8"))
            else:
                break
        finally:
            connection.close()
            
    
if __name__ == "__main__":
    start_server()
    
    