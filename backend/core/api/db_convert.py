import csv
import numpy as np
def csv_to_dataset(filename,data,target):
    with open(filename,"r",newline="") as f:
        output = {'data':[],'target':[]}
        reader = csv.reader(f)
        headers = next(reader)
        #print(headers)
        column_indexes = {'data':None,'target':None}
        for i in range(len(headers)):
            if headers[i] == data:
                column_indexes["data"] = i
            if headers[i] == target:
                column_indexes["target"] = i
        #print(column_indexes)
        for row in reader:
            output["data"].append(row[column_indexes["data"]])
            output["target"].append(row[column_indexes["target"]])
             
        
    return output