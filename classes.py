class Person:
    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f'Hi {self.name}!')


person = Person("Shlesh")
person.talk()


