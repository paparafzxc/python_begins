tasks = []


def store(task):
    tasks.append(task)


def modify(id, new_task):
    tasks[id] = new_task


def delete(id):
    tasks.pop(id)


def index():
    execute = 'n'
    while execute == 'n':
        try:

            job = input("What do you want to do? (add, mod, rem): ")
            if job == 'add':
                task = {
                    "task_name": input("Enter Task Name: "),
                    "is_complete": False
                }
                store(task)
                print(tasks)
            elif job == 'mod':
                id = int(input("Enter Task Index: "))
                new_task = {
                    "task_name": input("Enter New Task Name: "),
                    "is_complete": input("Update Status: ")
                }
                modify(id, new_task)
                print(tasks)
            elif job == 'rem':
                id = int(input("Enter Task Index: "))
                delete(id)
                print(tasks)
            else:
                print("Please Select One from the Menu")

        except Exception as e:
            print(f"Uh Oh {e}")

        execute = input("Do you wish to exit? (y /n): ")


index()


