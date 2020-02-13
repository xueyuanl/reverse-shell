import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 7676))
    s.listen(6)  # set the maximum connection

    sock, addr = s.accept()
    print('Get connection: {}'.format(addr[0]))

    while True:
        command = input('~$')
        sock.send(command.encode('utf-8'))

        data = sock.recv(1024).decode('utf-8')
        print(data)

    sock.close()
    s.close()


if __name__ == '__main__':
    main()
