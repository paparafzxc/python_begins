def func():
    amount = float(input("Total Amount: "))
    member = input("Member? Y or N: ")

    if amount >= 100 and member == 'Y':
        print("Qualified")
    else:
        print("Not Qualified")
    return func()
func()
