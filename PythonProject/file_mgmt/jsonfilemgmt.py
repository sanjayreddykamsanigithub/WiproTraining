import json
import os

def write_json(filename):
    data = [
        {"name": "John Doe", "age": 30},
        {"name": "Jane Smith", "age": 25}
    ]
def read_excel(filename):
    workbook = load_workbook(filename)
    sheet = workbook.active
    for row in sheet.iter_rows(values_only=True):
        print(f"Name: {row[0]}, Age: {row[1]}")

def delete_excel(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")

filename = "data.xlsx"
write_excel(filename)
print("Data read from Excel file:")
read_excel(filename)
delete_excel(filename)