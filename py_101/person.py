class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Doe")
john.talk()

bob = Person("Bob Ross")
bob.talk()


# DRY: Don't Repeat Yourself

