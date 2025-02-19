import csv

data = [
    {"name": "Alice", "age": 30, "city": "Seoul"},
    {"name": "Bob", "age": 25, "city": "Busan"}
]

with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)