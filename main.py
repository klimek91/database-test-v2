import csv
#wyswietlenie = input("Czy wyswietlic liste? (Y/N): ")

osoby = []

try:
    csv_file = open('lista.csv', "r")
    file = csv.reader(csv_file,delimiter=",")
    for row in file:
        osoba = {'id': int(row[0]), 'imie': row[1], 'pass': row[2]}
        print(osoba)
except FileNotFoundError:
    csv_file = open('lista.csv', 'w')
    writer = csv.writer(csv_file,delimiter=",")



