
def makefile(data):
    data_2 = data
    file = open('contact_info.txt', 'w')
    file.write("# File Contents:\n")
    file.write("# ====================\n")
    file.write(f"# {data_2}\n")
    file.write("# ====================\n")
    file.close()


def func():
    data = {
        "name" : input("Enter Name: "),
        "email": input("Enter Email: "),
        "age": int(input("Enter Age: ")),
        "phone": input("Enter Phone: ")
    }
    makefile(data)
    # print(data)


func()