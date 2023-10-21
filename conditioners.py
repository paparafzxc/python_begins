def func():
    temp = float(input("Enter Temp:"))
    print(f'Temperature is {temp}')
    if 25 <= temp < 30:
        print(f'Perfect \U0001f600')
    elif temp >= 30:
        print(f'Hot \U0001F606')
    else:
        print(f'Cold \U0001F923')
    return func()
func()