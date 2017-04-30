class Dog:
    def __init__(self, name : str):
        self.name = name

    def say_name(self) -> str:
        print(self.name,":","My name is",self.name)

    def bark(self):
        print(self.name,":","Bark Bark")
