from calc.my_functioners import *


def func():
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    operation = input("Operation : ")

    match operation:
        case 'sum':
            print(add(num1, num2))
        case 'subtract':
            print(subtract(num1, num2))
        case 'multiply':
            print(multiply(num1, num2))
        case 'divide':
            print(divide(num1, num2))

    return func()


func()




