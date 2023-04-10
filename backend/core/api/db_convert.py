import csv

#Repo style, data accessing locally, assuming schema

#Appends a dictionary of data to a CSV file with the given filename.
def append_data(filename: str, schema: dict, data: dict) -> int:
    if not data or not schema: return None
    #Assuming key 'time' is always present, main key of csv/data, and is unique locator
    with open(filename, 'r') as f: #adds the id to the data, based on row count
        reader = csv.reader(f)
        row = len(list(reader)) 
        if row == 0: row = 1 #if file empty, start at 1 cuz header insert later
        data['id'] = row
    with open(filename, 'a', newline='') as f:
        filekeys = ['id'] + list(schema.keys()) #so it writes id first col
        writer = csv.DictWriter(f, fieldnames=filekeys)
        if f.tell() == 0: #check if file empty
            writer.writeheader()        
        writer.writerow(data)
    return data.get('id')

#Retrieves a single row of data from a CSV file with the given filename.
def get_data(filename: str, schema: dict, time: str = None, id: int = None) -> dict:
    if (not time and id == None) or not schema: return None
    key, value = ('time', time) if time else ('id', id)
    with open(filename, 'r') as f:
        filekeys = ['id'] + list(schema.keys())
        reader = csv.DictReader(f, fieldnames=filekeys)
        for row in reader:
            if row.get(key) == str(value):
                return row
    return {}

#Retrieves all rows of data from a CSV file with the given filename.
def get_data_all(filename: str, schema: dict) -> list:
    if not schema: return None
    with open(filename, 'r') as f:
        filekeys = ['id'] + list(schema.keys())
        reader = csv.DictReader(f, fieldnames=filekeys)
        next(reader) #skip header
        return list(reader)