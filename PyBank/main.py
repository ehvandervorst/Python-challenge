import os
import csv

pybank = os.path.join("Resources", "budget_data.csv")

with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

def 


