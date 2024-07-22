from typing import Callable


def sum_profit(text: str, func: Callable):
    # Створюємо генерор функції та передаємо необідний текст
    func_generator_numbers = func(text)
    # Оголошуємо змінну доходу та обчислюємо зазначений в тексті дохід
    income_sum: float = 0
    for income_number in func_generator_numbers:
        income_sum += income_number
    return income_sum


def generator_numbers(text: str):
    # Розділяємо рядок на слова через роздільник "пробіл"
    word_list = text.split()
    # Шукаємо числові значення доходу і обробляємо можливі помилки перетворення формату
    for word in word_list:
        try:
            if word.replace(".", "").isdigit():
                yield float(word)
        except ValueError:
            print(f"Value Error. Number {word} has wrong format")


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
