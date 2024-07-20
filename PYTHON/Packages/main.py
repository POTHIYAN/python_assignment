from my_package.class_one import ClassOne # type: ignore
from my_package.class_two import ClassTwo # type: ignore

def main():
    # Creating objects of each class
    obj1 = ClassOne("Hello from ClassOne")
    obj2 = ClassTwo("Hello from ClassTwo")

    # Calling methods
    obj1.display()
    obj2.display()

if __name__ == "__main__":
    main()
