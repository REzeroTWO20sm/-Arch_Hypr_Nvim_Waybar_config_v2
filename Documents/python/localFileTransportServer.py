import socket
import zipfile

def start_server(host='127.0.0.1', port=1233, buffer_size=65536):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")

    with open('received_folder.zip', 'wb') as f:
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            f.write(data)
    print("File has been received successfully.")

    conn.close()
    server_socket.close()

    # Unzipping the received file
    with zipfile.ZipFile('received_folder.zip', 'r') as zip_ref:
        zip_ref.extractall('received_folder')  # Extract to a specific folder
    print("Folder has been extracted successfully.")


if __name__ == '__main__':
    start_server()

