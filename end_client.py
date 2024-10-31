import socket
import tkinter as tk
from tkinter import messagebox


class EndClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Конечный клиент")

        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack()

        self.update_button = tk.Button(
            self.root, text="Получить сообщения", command=self.get_messages)
        self.update_button.pack()

    def get_messages(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # SOCK_STREAM = TCP
                s.connect(('localhost', 1503))
                data = b""
                while True:
                    part = s.recv(1024)  # получает до 1024 байтов за раз
                    if not part:
                        break
                    data += part

                # чтоб UnicodeDecodeError не показывался?
                messages = data.decode('utf-8', errors='ignore')
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, messages)

        except ConnectionRefusedError:
            messagebox.showerror(
                "Ошибка", "Не удалось подключиться к промежуточному клиенту.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EndClientApp(root)
    root.mainloop()
