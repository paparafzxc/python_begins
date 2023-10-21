def to_fahrenheit(temp):
    # C ×  (9 / 5) + 32
    result = temp * (9/5)+32
    return result


def to_celsius(temp):
    # (F − 32) × 5/9
    result = (temp - 32) * 5/9
    return result


def convert():
    try:
        temp = float(input("Enter Temperature: "))
        convert_to = input("Convert To (F / C): ")

        if convert_to == 'F':
            print(to_fahrenheit(temp))
        elif convert_to == 'C':
            print(to_celsius(temp))
        else:
            print('Invalid Input. Try Again')

    except Exception as e:
        error = type(e)
        print(f'Exception Found: {error}')

    return convert()


convert()