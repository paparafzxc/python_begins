from prettytable import PrettyTable

name = input("Name:")
age = int(input("Age:"))

data = {
    "name": name,
    "age": age
}

t = PrettyTable(['name', 'age'])
t.add_row([data['name'], data['age']])
print(t)

