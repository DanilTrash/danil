import configparser
import socket


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    server = config['server']['host'], int(config['server']['port'])
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect(server)
        message = input("-> ")
        while message != 'q':
            sock.sendto(message.encode('utf-8'), server)
            data, addr = sock.recvfrom(1024)
            data = data.decode('utf-8')
            print("Received from server: " + data)
            message = input("-> ")


if __name__ == '__main__':
    main()
