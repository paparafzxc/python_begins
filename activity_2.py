def add(x, y):
    result = x + y
    return result


def sub(x, y):
    result = x - y
    return result


def mult(x, y):
    result = x * y
    return result


def div(x, y):
    result = x / y
    return result


def calc():
    prompt = 'y'
    while prompt == 'y':
        try:
            x = float(input("1st Num: "))
            y = float(input("2nd Num: "))
            opr = input("Select Arithmetic Operation (+, -, *, /): ")

            if opr == '+':
                print(add(x, y))
            elif opr == '-':
                print(sub(x, y))
            elif opr == '/':
                print(div(x, y))
            elif opr == '*':
                print(mult(x, y))
            else:
                print('Invalid Input. Try Again')

            prompt = input('Do you want more? (y / n): ')

        except Exception as e:
            # error = type(e)
            print(f'Exception Found: {e}')

    # return calc()


calc()