import threading
import time

# Общий счетчик
counter = 0

# Reentrant Lock для синхронизации потоков (аналог ReentrantLock в Java)
rlock = threading.RLock()

# Функция для инкрементирования счетчика


def increment_counter():
    global counter
    for _ in range(100000):
        rlock.acquire()  # Захватываем блокировку
        try:
            counter += 1  # Инкрементируем счётчик
        finally:
            rlock.release()  # Освобождаем блокировку

# Функция для декрементирования счетчика


def decrement_counter():
    global counter
    for _ in range(100000):
        rlock.acquire()  # Захватываем блокировку
        try:
            counter -= 1  # Декрементируем счётчик
        finally:
            rlock.release()  # Освобождаем блокировку

# Главная функция для запуска потоков


def run_threads(n, m):
    global counter
    counter = 0  # Инициализируем счётчик
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
run_threads(5, 5)  # Равное количество потоков для инкремента и декремента
