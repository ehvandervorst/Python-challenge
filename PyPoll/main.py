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
        candidates.append(row[2])
    
    print("Election Results")
    print("-----------------")
    print("Total Votes:", len(votes))
    print("-----------------")

    import collections
    results = collections.Counter(candidates)
    for key, val in results.items():
        print('{}: ({})'.format(key,val))
    
    from statistics import mode
    winner = mode(candidates)
    
    #vote_percentage = vote_counts/len(votes)*100
  
    print("-----------------")
    print(f"Winner: {winner}")
    print("-----------------")

#import sys
#import os.path

#orig = sys.stdout
#with open(os.path.join(parent_dir, "Analysis", "finance.txt"), "wb") as f:
    #sys.stdout = f
    #exec(open("./main.py").read())
    #sys.stdout = orig