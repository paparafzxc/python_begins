from datetime import date

fname = input("First Name:")
lname = input("Last Name:")
year = int(input("Birth Year:"))
month = int(input("Birth Month:"))
day = int(input("Birth Day:"))

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
age = age(date(year, month, day))
print(f'My name is {fname} {lname} and I am {age} yrs old.')