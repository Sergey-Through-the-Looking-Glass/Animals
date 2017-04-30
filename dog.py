class Dog:
    def __init__(self, name : str):
        self.name = name

    def say_name(self) -> str:
        print(self.name,":","Yarr,",self.name,"is here!")

    def bark(self):
        print(self.name,":","Bark Bark")

    def bite(self, target):
        target.get_hurt_by(self)
