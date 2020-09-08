import os
import csv

parent_dir = os.path.abspath(os.path.dirname(__file__))
pybank = os.path.join(parent_dir, 'Resources','budget_data.csv')

with open(pybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

def print_results(pybank):
    month = str(pybank[0])
    profit_loss = float(pybank[1])
    revenue = [2]
    date = [3]
    rev_change = [4]

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", len(month))
    print("Total: $", sum(profit_loss))

    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i - 1])
        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)
        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])

    print(f"Average Change: $", round(avg_rev_change))
    print(f"Greatest Increase in Profits:", max_rev_change_date, "($", max_rev_change,")")
    print(f"Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")

