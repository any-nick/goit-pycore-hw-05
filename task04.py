def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ in ["add_contact", "change_contact"]:
                return "ValueError: Name and phone are missing. Please specify them in the command."
            elif func.__name__ in ["show_phone"]:
                return "ValueError: Name is missing. Please specify it in the command."
            else:
                return "ValueError: unknown error. Please contact support."
        except IndexError:
            return "IndexError: Argument is missing. Check your input."
        except KeyError:
            return "KeyError: Name was not found in dictionary. Please create new contact or check input name."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    else:
        contacts[name] = phone
        return "Contact added."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name} phone is {contacts[name]}"


def show_all(contacts):
    result = "List of stored contacts:\n"
    for key, value in contacts.items():
        result += f"{key}: {value}\n"
    return result.strip()


@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts[name]:
        contacts[name] = phone
        return "Phone was changed."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
