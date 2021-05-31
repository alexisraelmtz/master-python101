class Mamals:
    def walk(self):
        print("Walk")


class Dog(Mamals):
    def bark(self):
        print("Bark")


class Cat(Mamals):
    def annoy(self):
        print("Miau")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.annoy()
