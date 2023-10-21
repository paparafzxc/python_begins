companies = []


def store(company):
    companies.append(company)


def modify(id, new_comp):
    companies[id] = new_comp


def delete(id):
    companies.pop(id)


def index():
    job = input("What do you want to do? (add, mod, rem): ")
    if job == 'add':
        comp = input("Enter Company: ")
        store(comp)
        print(companies)
    elif job == 'mod':
        id = int(input("Enter Index: "))
        new_comp = input("New Value: ")
        modify(id, new_comp)
        print(companies)
    elif job == 'rem':
        id = int(input("Enter Index: "))
        delete(id)
        print(companies)
    else:
        print(companies)

    return index()

index()





