import socket
import threading


class ProxyClient:
    def __init__(self):
        self.sock_udp = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock_udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock_udp.bind(('', 1502))

        group = socket.inet_aton('233.0.0.1')
        mreq = group + socket.inet_aton('0.0.0.0')
        self.sock_udp.setsockopt(
            socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        self.last_message = None
        self.recent_messages = []

        self.sock_tcp = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # создает TCP-сокет
        self.sock_tcp.bind(('', 1503))
        self.sock_tcp.listen(5)

    def listen_udp(self):
        while True:
            data, _ = self.sock_udp.recvfrom(1024)  # получает сообщение
            message = data.decode('utf-8')
            if message != self.last_message:
                print(f"Новое сообщение: {message}")
                self.last_message = message
                self.recent_messages.append(message)
                if len(self.recent_messages) > 5:
                    self.recent_messages.pop(0)

    def handle_tcp_client(self, client_socket):
        recent_messages = "\n".join(self.recent_messages)
        client_socket.sendall(recent_messages.encode('utf-8'))
        client_socket.close()

    def listen_tcp(self):
        while True:
            # ожидает подключения от конечного клиента
            client_socket, _ = self.sock_tcp.accept()
            threading.Thread(target=self.handle_tcp_client,
                             args=(client_socket,)).start()

    def run(self):
        threading.Thread(target=self.listen_udp).start()
        self.listen_tcp()


if __name__ == "__main__":
    proxy_client = ProxyClient()
    proxy_client.run()
