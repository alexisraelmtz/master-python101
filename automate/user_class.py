# Py OOP


class Developers:
    raise_amount = 1.5
    devs_count = 0

    def __init__(self, first, last, pay):
        # self.self = self
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.net"
        Developers.devs_count += 1

    def fullname(self):
        return f"{self.first} {self.last}"
        # Method

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


user1 = Developers("Alex", "Martinez", 7_000)
user2 = Developers("Dev", "Test", 4_500)

print(user1.email)
print(user2.fullname())
print(Developers.fullname(user1))

print(f"\nNumber of active users: {Developers.devs_count}")

print(f"\nDefault raise amount not applied: {Developers.raise_amount}")
user2.get_raise()
print(f"Aplying 1st default raise: {user2.pay:$=9,.2f}")
Developers.change_raise(3.5)
print(f"Changed, not applied raise: {user2.raise_amount}")
print(f"Pay is the same: {user2.pay:$=9,.2f}")
user2.get_raise()
print(f"Commited raise: {user2.pay:$=10,.2f}")

user_form3 = "John-Doe-7_000"
user_form4 = "Steve-Smith-6_500"
user_form5 = "Will-Miller-5_500"

new_user3 = Developers.user_db(user_form3)
new_user4 = Developers.user_db(user_form4)
new_user5 = Developers.user_db(user_form5)

print(f"\nNumber of active users: {Developers.devs_count}")
print(new_user3.email)
print(new_user4.fullname())

import datetime

day = datetime.date(2020, 9, 8)

print(f"\n{Developers.is_worked(day)}")