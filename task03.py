import sys


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("FileNotFoundError: File Not Found")
            sys.exit(1)
        except UnicodeDecodeError:
            print("UnicodeDecodeError: The file is possibly corrupted")
            sys.exit(1)
        except IndexError:
            print("IndexError: Incorect command. Please check your input")
            sys.exit(1)
        except KeyError:
            print("KeyError: Check your log file")
            sys.exit(1)
        except ValueError:
            print("ValueError: Check your log file")
            sys.exit(1)
    return inner


def load_logs(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        loaded_data = file.readlines()
    return [parse_log_line(line) for line in loaded_data]


def parse_log_line(line: str) -> dict:
    # Розділяємо рядок на 4 частини
    date, time, log_severity, message = line.split(maxsplit=3)
    # Формуємо словник
    return {
        "date": date,
        "time": time,
        "log_severity": log_severity.upper(),
        "message": message.strip()
    }


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = list(
        filter(lambda logs: logs["log_severity"] == level.upper(), logs))
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    # Визначаємо кількість можливих рівнів логів
    severity_levels = {log["log_severity"] for log in logs}
    # Створюємо пустий словник для збереження значень
    counted_logs_by_severity = {}
    # Обраховуємо кількість логів згідно кожного унікального рівня
    for severity in severity_levels:
        res = len(
            list(filter(lambda logs: logs["log_severity"] == severity.upper(), logs)))
        counted_logs_by_severity.update({severity: res})

    return counted_logs_by_severity


def display_log_counts(parsed_file: dict):
    # Знаховимо максимальну ширину змінної severity
    max_key_length = max(len(level) for level in parsed_file.keys())
    # Знаховимо максимальну ширину змінної count
    max_value_length = max(len(level) for level in parsed_file.keys())
    # Знаховимо максимальну ширину першого стовпчика, але не меншу ніж його назва
    first_column_length = max_key_length if max_key_length > 14 else 14
    # Знаховимо максимальну ширину другого стовпчика, але не меншу ніж його назва
    second_column_length = max_value_length if max_value_length > 5 else 5
    # Виводимо заголовок
    print(f"{"Severity level":<{first_column_length}} | Count")
    print(f"{'-' * first_column_length} | {'-' * second_column_length}")
    # Виводимо значення з словника
    for severity, count in parsed_file.items():
        print(f"{severity:<{first_column_length}} | {count}")


@input_error
def main():
    # Огологуємо і присвоюємо аргементи командного рядка змінним
    path_to_file = sys.argv[1]
    # Перевіряємо чи є другий необов'язковий аргумент
    if len(sys.argv) == 3:
        severity_filter = sys.argv[2].lower()
    else:
        severity_filter = None
    # Викликаємо функцію для отримання опрацьованих даних
    parsed_file = load_logs(path_to_file)
    # Рахуємо та виводимо кількість логів кожного рівня
    log_severity_dict = count_logs_by_level(parsed_file)
    display_log_counts(log_severity_dict)
    # Виводимо додаткові логи згідно рівня, який був заданий в команді
    if severity_filter != None:
        filreted_logs = filter_logs_by_level(parsed_file, severity_filter)
        if not filreted_logs:
            print(
                f"\nNo logs were found by specified filter {severity_filter.upper()}.")
        else:
            print(
                f"\nDetails logs of severity level \"{severity_filter.upper()}\":")
            for item in filreted_logs:
                print(
                    f"{item["date"]} {item["time"]} {item["log_severity"]} {item["message"]}")


if __name__ == "__main__":
    main()
