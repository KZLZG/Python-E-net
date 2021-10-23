from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from rich import print

def main():
    r = Rectangle("синего", 20, 20)
    c = Circle("зеленого", 20)
    s = Square("красного", 20)
    print("[italic blue]Этот", r)
    print("[italic green]Этот",c)
    print("[italic red]Этот",s)

if __name__ == "__main__":
    main()