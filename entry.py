#!python

from dog import Dog

print("hello")

def f():
    return "f"

if __name__ == '__main__':
    dog = Dog("Rammstein")
    dog.say_name()
    dog.bark()
