import csv

rows = [["name", "age"], ["Sara", 22], ["Omid", 25]]
with open("people.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)

with open("people.csv") as f:
    for row in csv.reader(f):
        print(row)
