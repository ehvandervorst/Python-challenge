import os
import csv

pybank = os.path.join("Resources", "budget_data.csv")

with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    revenue = []
    date = []
    rev_change[]

    revenue.append(float(row[1]))
    date.append(row[0])

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months:" len(date))
    print(f"Total:", sum(revenue))

  for i in range(1,len(revenue)):
      rev_change.append(revenue[i] - revenue[i - 1])
      


    print(f"Average Change: {str(average_pl)}")
    print(f"Greatest Increase in Profits: {str(increase)}")
    print(f"Greatest Decrease in Profits: {str(decrease)}")
