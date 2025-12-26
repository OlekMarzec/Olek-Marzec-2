class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w mieście {self.city}, ul. {self.street}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}"


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka: {self.author_surname} {self.author_name} ({self.library})"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        ksiazki_str = ", ".join([str(b) for b in self.books])
        return (f"Zamówienie z dnia {self.order_date}\n"
                f"Obsługa: {self.employee}\n"
                f"Klient: {self.student}\n"
                f"Pozycje: {ksiazki_str}")


lib1 = Library("Warszawa", "Złota 1", "00-001", "8-16", "111-222-333")
lib2 = Library("Kraków", "Smocza 2", "30-002", "9-17", "444-555-666")

emp1 = Employee("Jan", "Kowalski", "2020-01-01", "1990-05-05", "Warszawa",
                "Prosta", "00-002", "999-888-777")
emp2 = Employee("Anna", "Nowak", "2021-03-15", "1992-07-07", "Kraków",
                "Krzywa", "30-003", "666-555-444")
emp3 = Employee("Piotr", "Wiśniewski", "2019-11-20", "1985-12-12", "Gdańsk",
                "Długa", "80-001", "333-222-111")

stud1 = "Marek Zięba"
stud2 = "Kasia Wójcik"
stud3 = "Tomek Mazur"

b1 = Book(lib1, "2000", "Adam", "Mickiewicz", 300)
b2 = Book(lib1, "2005", "Juliusz", "Słowacki", 250)
b3 = Book(lib2, "2010", "Henryk", "Sienkiewicz", 500)
b4 = Book(lib2, "2015", "Bolesław", "Prus", 600)
b5 = Book(lib1, "2020", "Stanisław", "Lem", 350)

order1 = Order(emp1, stud1, [b1, b2], "2023-10-01")
order2 = Order(emp2, stud2, [b3, b4, b5], "2023-10-02")

print(order1)
print("-" * 20)
print(order2)
