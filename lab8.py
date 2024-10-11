import threading
import time
import platform

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

    # Вычисляем время выполнения
    execution_time = (time.time() - start_time) * 1000  # Время выполнения в мс
    return counter, execution_time


# Запуск программы с различными наборами потоков
results = []
for threads in [1, 2, 4, 8]:
    counter_value, exec_time = run_threads(threads, threads)
    results.append((threads, counter_value, exec_time))

# Получение спецификации системы
system_spec = f"OS: {platform.system()} {platform.release()}\n" \
    f"Processor: {platform.processor()}\n" \
    f"Memory (RAM): {
    round(int(platform.uname().version.split()[2]) / (1024**2), 2)} GB\n"

# Сохранение результатов в файл
table = "Threads | Counter Value | Execution Time (ms)\n"
table += "----------------------------------------------\n"
for result in results:
    table += f"{result[0]:<7} | {result[1]:<13} | {result[2]:<18.2f}\n"

full_output = system_spec + "\n" + table

# Сохраняем в файл Lab8.txt
with open("/mnt/data/Lab8.txt", "w") as file:
    file.write(full_output)
