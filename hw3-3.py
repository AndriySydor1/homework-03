'''  Напишіть реалізацію функції factorize, яка приймає список чисел та повертає список чисел, на які числа з вхідного списку поділяються без залишку.
Реалізуйте використання кількох ядер процесора для паралельних обчислень і замірте час виконання знову.
 Для визначення кількості ядер на машині використовуйте функцію cpu_count() з пакета multiprocessing    
''' 


import time
import multiprocessing
from multiprocessing import Pool, freeze_support

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    with Pool(multiprocessing.cpu_count()) as pool:
        result = pool.map(get_factors, numbers)
    return result

if __name__ == '__main__':
    freeze_support()  # Додаємо цей рядок

    # Перевірка правильності алгоритму
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    print("Паралельна версія працює правильно.")

    # Вимірювання часу виконання паралельної версії
    start_time = time.time()
    factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"Паралельна версія виконана за {end_time - start_time:.4f} секунд")
    





