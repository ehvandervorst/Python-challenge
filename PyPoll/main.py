import os
import csv

parent_dir = os.path.abspath(os.path.dirname(__file__))
pypoll = os.path.join(parent_dir, "Resources", "election_data.csv")

with open(pypoll) as polling_data:
    reader = csv.reader(polling_data, delimiter=',')
    next(reader)

    votes = []
    candidates = []

    for row in reader:
        votes.append(float(row[0]))
        candidate.append(row[2])

    for i in range(1,len(votes)):
        

    print("Election Results")
    print("-----------------")
    print("Total Votes:", len(votes))
    print("-----------------")
    print("-----------------")
    print("Winner:")
    print("-----------------")