#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    s1 = Square(5)
    print(r1.__class__.__name__)
    print(s1.__class__.__name__)
    Rectangle.save_to_file([r1, r2])
    Square.save_to_file([s1])

    with open("Rectangle.json", "r") as file:
        print(file.read())
