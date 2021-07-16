# Py OOP


import datetime


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


user1 = Developers("Alex", "Martinez", 7_000)
user2 = Developers("Dev", "Test", 4_500)

# reversed()

print(user1.email)
print(user2.fullname)
print(user1.fullname)

print(f"\nNumber of active users: {Developers.devs_count}")

print(f"\nDefault raise amount not applied: {Developers.raise_amount}")
user2.get_raise()
print(f"Aplying 1st default raise: {user2.pay:$=9,.2f}")
Developers.change_raise(3.5)
print(f"Changed, not applied raise: {user2.raise_amount}")
print(f"Pay is the same: {user2.pay:$=9,.2f}")
user2.get_raise()
print(f"Commited raise: {user2.pay:$=10,.2f}")

user_form3 = "John-Doe-7000"
user_form4 = "Steve-Smith-6500"
user_form5 = "Will-Miller-5500"

new_user3 = Developers.user_db(user_form3)
new_user4 = Developers.user_db(user_form4)
new_user5 = Developers.user_db(user_form5)

print(f"\nNumber of active users: {Developers.devs_count}")
print(new_user3.email)
print(new_user4.fullname)


day = datetime.date(2020, 9, 17)


print(f"\nToday is a: {Developers.is_worked(day)}")

print("\nNew Class Inheritance: Employees ...")


class Employee(Developers):
    raise_amount = 1.15

    def __init__(self, first, last, pay, place):
        super().__init__(first, last, pay)
        self.place = place


new_user6 = Employee("Johnathan", "Rogan", 3_600, "CEO")

print(new_user6.email)
print(new_user6.place)
print(f"Without raise applied: {new_user6.pay:$=9,.2f}")
new_user6.get_raise()
print(f"With raise: {new_user6.pay:$=9,.2f}")

print(f"\nNumber of active users: {Developers.devs_count}")

print("\nNew Class Inheritance: Managers ...")


class Manager(Developers):
    def __init__(self, first, last, pay, developers=None):
        super().__init__(first, last, pay)
        if developers is None:
            self.developers = []
        else:
            self.developers = developers

    def add_dev(self, devs):
        for dev in devs:
            if dev not in self.developers:
                self.developers.append(dev)

    def remove_dev(self, dev):
        if dev in self.developers:
            self.developers.remove(dev)

    def list_devs(self):
        for i, dev in enumerate(self.developers, start=1):
            print(f"{i} --- {dev.fullname}")


new_user7 = Employee("Edith", "Macias", 7_800, "Chemist")
new_user8 = Employee("Armando", "Barajas", 6_600, "Coder")

mgr1 = Manager("Sue", "Lee", 9_000, [new_user6])
print(mgr1.email)
mgr1.list_devs()
print(f"Assigning new developers to Mangaer: {mgr1.fullname}")
mgr1.add_dev([new_user7, new_user8])
mgr1.remove_dev(new_user6)
mgr1.list_devs()

print(f"\nNumber of active users: {Developers.devs_count}")

print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developers))
print(isinstance(mgr1, Manager))
# Is an Object instance of a Class: "isinstance()"
# Is a class subclass of an other Class: "issubclas()"
print(issubclass(Developers, Employee))
print(issubclass(Employee, Developers))
print(issubclass(Developers, Manager))
print(issubclass(Manager, Developers))

print(f"\n{new_user3}")
print(f"{new_user3.__repr__()}")
print(f"{new_user3.__str__()}")
x = user1 + user2
print(f"{x:$=10,.2f}\n")

# user2 = Developers("Dev", "Test", 4_500)
print(user2.__repr__())
user2.fullname = "ChangedDev Test2"
print(user2.fullname)
print(user2.__repr__())
del user2.fullname
