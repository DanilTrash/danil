import socket
import configparser


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    server = config['server']['host'], int(config['server']['port'])
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(server)
        print("Server Started")
        while True:
            data, addr = sock.recvfrom(1024)
            data = data.decode('utf-8')
            print("Message from: " + str(addr))
            print("From connected user: " + data)
            data = data.upper()
            print("Sending: " + data)
            sock.sendto(data.encode('utf-8'), addr)


if __name__ == '__main__':
    main()
