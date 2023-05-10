

class Phonebook:

    class Contact:
        def __init__(self, name, phone):
            self.name = name
            self.phone = phone

        def change_phone(self, new_phone):
            self.phone = new_phone

    def __init__(self):
        self.contacts = []

    @staticmethod
    def len_contact():
        return 10

    def add_contact(self, name, phone):
        contact = Phonebook.Contact(name, phone)
        return contact

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def print_contacts(self):
        print("Контакты:")
        for contact in self.contacts:
            print(f"{contact.name}: {contact.phone}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"{contact.name}: {contact.phone}")

pb = Phonebook()

contact1 = pb.add_contact("Иван Иванов", "+7 (111) 111-11-11")
contact2 = pb.add_contact("Петр Петров", "+7 (222) 222-22-22")

contact3 = pb.add_contact("Сергей Сергеев", "+7 (333) 333-33-33")

contact1.change_phone("+7 (444) 444-44-44")

pb.print_contacts()

pb.search_contact("Петр Петров")

print(Phonebook.len_contact())
print(pb.len_contact())