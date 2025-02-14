import socket
import os
import zipfile
import shutil

def compress_folder(folder_path):
    zip_path = f"{folder_path}.zip"
    shutil.make_archive(folder_path, 'zip', folder_path)
    return zip_path

def send_file(file_path, host='192.168.56.101', port=1233):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            client_socket.sendall(data)

    print(f"File '{os.path.basename(file_path)}' has been sent successfully.")
    client_socket.close()

if __name__ == '__main__':
    folder_path = "/home/zero/DS2Copy/"  # Specify the path of the folder you want to send
    zip_path = compress_folder(folder_path)
    send_file(zip_path)

