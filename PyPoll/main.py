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
        if row[2] not in candidates:
            candidates.append(row[2])
    
    print("Election Results")
    print("-----------------")
    print("Total Votes:", len(votes))
    print("-----------------")

# (number of votes) count instances of each candidate  
# (percent of votes) divide each candidate's number of votes against len(votes)
# (determine winner) winner is candidate with most votes
    
    print("-----------------")
    print("Winner:")
    print("-----------------")