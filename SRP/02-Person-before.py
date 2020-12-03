class Person:
    def __init__(self, name, phone, office_code):
        self.name = name
        self.phone = phone
        self.office_code = office_code

    def phone_number_of(self):
        return f'{self.phone} add {self.office_code}'


person = Person('Kolyan', '23-21', 1)
print(person.phone_number_of())
