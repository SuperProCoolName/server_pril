import socket
import time


def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) 
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2) # TTL = time to live

    while True:
        with open('message.txt', 'r', encoding='utf-8') as f:
            message = ''
            for line in f:
                message += line.strip()
                message += '\n'

        sock.sendto(message.encode('utf-8'), ('233.0.0.1', 1502))
        print(f"Отправлено сообщение: {message}")
        time.sleep(10)


if __name__ == "__main__":
    start_server()
