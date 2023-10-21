def func():
    age = float(input("Enter Age:"))

    has_id = False
    if age >= 18:
        print('Age is Good')
        if has_id:
            print("Come Inside! \U0001f600")
        else:
            print("But you need ID")
    else:
        print("Too Young")

    # elif temp >= 30:
    #     print(f'Hot \U0001F606')
    # else:
    #     print(f'Cold \U0001F923')
    return func()
func()