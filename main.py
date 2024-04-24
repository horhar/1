class Application:
    def __init__(self):
        self.address_book = AddressBook()
        self.task_list = TaskList()

    def run(self):
        while True:
            print("\n1. Додати контакт")
            print("2. Показати всі контакти")
            print("3. Додати завдання")
            print("4. Показати всі завдання")
            print("5. Вийти")

            choice = input("Виберіть опцію: ")

            if choice == '1':
                name = input("Введіть ім'я контакту: ")
                phone = input("Введіть номер телефону: ")
                email = input("Введіть електронну адресу: ")
                contact = Contact(name, phone, email)
                self.address_book.add_contact(contact)
                print("Контакт успішно доданий!")

            elif choice == '2':
                print("\nСписок контактів:")
                self.address_book.display_contacts()

            elif choice == '3':
                description = input("Введіть опис завдання: ")
                priority = input("Введіть пріоритет завдання: ")
                due_date = input("Введіть крайній термін завдання (якщо є): ")
                task = Task(description, priority, due_date)
                self.task_list.add_task(task)
                print("Завдання успішно додане!")

            elif choice == '4':
                print("\nСписок завдань:")
                self.task_list.display_tasks()

            elif choice == '5':
                print("Дякую за використання програми!")
                break

            else:
                print("Неправильний вибір. Будь ласка, виберіть знову.")

class Task:
    def __init__(self, description, priority, due_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        if self.due_date:
            return f"Task: {self.description}, Priority: {self.priority}, Due Date: {self.due_date}"
        else:
            return f"Task: {self.description}, Priority: {self.priority}"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

if __name__ == "__main__":
    app = Application()
    app.run()
