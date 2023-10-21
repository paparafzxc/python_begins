import csv

with open('MOCK_DATA.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

with open('new_csv.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age'])
    csv_writer.writerow(['Alice', 12])