'''
Выделение класса — приём рефакторинга, при котором из большого класса с множеством слабо-связанных 
по смыслу полей и методов, выделяется один или несколько классов.
Смысл приёма в том, чтобы явно выделить назначение класса. Идеальный результат — получить класс, 
который можно описать одной фразой или даже одним словом.
'''


class IPhoneNumber:
    def __init__(self, phone, office_code):
        self.phone = phone
        self.office_code = office_code

    def value_of(self):
        pass


class PhoneNumber(IPhoneNumber):
    def __init__(self, phone, office_code):
        IPhoneNumber.__init__(self, phone, office_code)
        self.phone = phone
        self.office_code = office_code

    def value_of(self):
        return f'{self.phone} add {self.office_code}'


class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def phone_number_of(self):
        return self.phone_number.value_of()


person = Person('Kolyan', PhoneNumber('23-21', 1))
print(person.phone_number_of())
