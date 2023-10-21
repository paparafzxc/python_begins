try:
    number = int(input("enter number: "))
    print(number)
except Exception as e:
    error = type(e)
    print(error)
finally:
    print("Yeah")

print("Exit.")