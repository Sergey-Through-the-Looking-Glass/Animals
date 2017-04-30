class Cat:
    def __init__(self, name : str):
        self.name = name

    def say_name(self) -> str:
        print(self.name,":","Meow, I am",self.name)

    def mew(self):
        print(self.name,":","Meow Meow")

    def scratch(self, target):
        target.get_hurt_by(self)
