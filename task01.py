def caching_fibonacci():
    # Створюємо пустий словник для кешування значень обчислення
    cache = {}

    def fibonacci(n):
        if n < 0:
            return 0
        elif n == 1:
            return 1
        # Перевіряємо наявність результатів обчислення в кеш-словнику
        elif n in cache:
            return cache[n]
        # Обчислюємо число фібоначі
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    # Повертаємо внутрішню функцію як результат зовнішньої
    return fibonacci


def main():
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610


if __name__ == "__main__":
    main()
