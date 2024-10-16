def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts: dict):
    name, phone = args
    if name.capitalize() not in contacts:
        return "Name not found in contacts"
    else:
        contacts.update({name.capitalize(): phone})
    return "Contact update"

@input_error
def show_phone(args, contacts: dict):
    name = args[0]
    name = name.capitalize()
    return f"{name} not found in contacts " if name not in contacts else contacts[name]

def show_all(contacts: dict):
    result = []
    for key, value in contacts.items():
        result.append(f"Name: {key.capitalize()} phone: {value}")
    return "\n".join(result)

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
        elif command == "phone":
            print(show_phone(args ,contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()