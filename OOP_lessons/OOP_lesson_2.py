class Person:
    def __init__(self, name, city, birth_year):
        self.name = name
        self.city = city
        self.birth_year = birth_year

    def get_age(self):
        return 2024 - self.birth_year


person = Person("Timur", "Izhevsk", 2003)
print("Age: ", person.get_age())
