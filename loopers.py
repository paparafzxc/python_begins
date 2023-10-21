# For
# cars = ['BumbleBee', 'Optimus Prime', 'McQueen', 'Angkas', 'Grab Taxi']
# for car in cars:
#     print(f'My Favorite Car is {car}')

# While
# count = 10
# while count > 0:
#     print(f'{count}')
#     count -= 1
# print('Blast OFF!')

from prettytable import PrettyTable

t = PrettyTable(['num1', 'num2', 'product'])
for x in range(1, 11):
    for y in (range(1, 11)):
        t.add_row([x, y, x*y])
print(t)