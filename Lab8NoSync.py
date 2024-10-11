import threading
import time

# Общий счетчик
counter = 0

# Блокировка для синхронизации потоков
lock = threading.Lock()

# Функция для инкрементирования счетчика


def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

# Функция для декрементирования счетчика


def decrement_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter -= 1

# Главная функция, которая создает и запускает потоки


def run_threads(n, m):
    global counter
    counter = 0  # Инициализируем счетчик
    threads = []

    # Создаем n потоков для инкремента
    for _ in range(n):
        t = threading.Thread(target=increment_counter)
        threads.append(t)

    # Создаем m потоков для декремента
    for _ in range(m):
        t = threading.Thread(target=decrement_counter)
        threads.append(t)

    # Засекаем время выполнения
    start_time = time.time()

    # Запускаем все потоки
    for t in threads:
        t.start()

    # Ожидаем завершения всех потоков
    for t in threads:
        t.join()

    # Выводим результат
    print(f'Значение общего счетчика: {counter}')
    print(f'Время выполнения: {time.time() - start_time:.4f} секунд')


# Пример запуска программы
run_threads(5, 5)  # 5 потоков инкремента и 5 потоков декремента
