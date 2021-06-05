def read_contacts():
    contacts = {}
    while True:
        text = input()
        if text.isnumeric():
            break
        name, phone = text.split('-')
        contacts[name] = phone

    return contacts, int(text)


def print_contact(contacts, n):
    for _ in range(n):
        name = input()

        if name in contacts:
            print(F"{name} -> {contacts[name]}")
        else:
            print(F"Contact {name} does not exist.")


contacts, n = read_contacts()
print_contact(contacts, n)
