#!python

from dog import Dog
from cat import Cat

print("hello")

def f():
    return "f"

if __name__ == '__main__':
    dog = Dog("Rammstein")
    cat = Cat("Snow")
    dog.say_name()
    dog.bark()
    cat.say_name()
    cat.mew()

