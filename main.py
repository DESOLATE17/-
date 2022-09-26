from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 3, 2)
    r1 = Rectangle("белого", 4, 4)
    c = Circle("зеленого", 5)
    c1 = Circle("красного", 3)
    s = Square("красного", 5)
    s1 = Square("синего", 6)
    print(r)
    print(c)
    print(s)
    print(r > r1)
    print(c > c1)
    print(s == s1)
    lst = [c,r,s]
    print(lst)
    lst.sort()
    print(lst)
if __name__ == "__main__":
    main()  