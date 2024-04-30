# Ana Robles
# CIS129
# Module 12 Lab: Create a Pet Class 
# 4/29/2024
# This program is for creating and displaying information about pets.

class Pet:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0

    def setName(self, n):
        self.name = n

    def setType(self, t):
        self.type = t

    def setAge(self, a):
        self.age = a

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


def main():
    inputName = input("Enter a pet name: ")
    inputType = input("Enter a pet type: ")
    inputAge = int(input("Enter a pet age: "))

    animal = Pet()
    animal.setName(inputName)
    animal.setType(inputType)
    animal.setAge(inputAge)

    print("The pet name is", animal.getName())
    print("The pet type is", animal.getType())
    print("The pet age is", animal.getAge())


if __name__ == "__main__":
    main()