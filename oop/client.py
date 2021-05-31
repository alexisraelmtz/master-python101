# Py OOP


class Developers:
    raise_amount = 1.5
    devs_count = 0

    def __init__(self, first, last, pay):
        # __init__: special Method
        self.first = first
        self.last = last
        self.pay = pay
        Developers.devs_count += 1

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.net"
        # property Decorator: defines a Method to access as a Atribute.
        # e.g. Without the parenthesis"( )".

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
        # Method

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleting Name ...")
        self.first = None
        self.last = None

    def get_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # Method

    @classmethod
    def change_raise(cls, amount):
        cls.raise_amount = amount
        # cls = (Developers) instead of the Instance: user1
        # Class method w/decorator: Developers.raise_amount = X%

    @classmethod
    def user_db(cls, user_form):
        first, last, pay = user_form.split("-")
        return cls(first, last, pay)
        # cls = (user1 = Developers)
        # Alternative Constructor

    @staticmethod
    def is_worked(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "NOT a working day"
        return "Working Day!"

    def __repr__(self):
        return f"{self.first} {self.last} - {self.email}"

    def __str__(self):
        return f"Developer('{self.first}', '{self.last}', '{self.pay}', '{self.email}')"

    def __add__(self, other):
        return self.pay + other.pay