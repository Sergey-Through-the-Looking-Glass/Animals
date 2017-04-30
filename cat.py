class Cat:
    def __init__(self, name : str):
        self.name = name

    def say_name(self) -> str:
        print(self.name,":","My name is",self.name)

    def mew(self):
        print(self.name,":","Meow Meow")
