import os
import csv

polling_data = os.path.join("Resources", "election_data.csv")
with open(polling_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

def print_data(polling_data):
    votes = int(polling_data[0])
    county = str(polling_data[1])
    candidate = str(polling_data[2])

    total_votes = 
    all_candidate =
    percent_votes = 
    candidate_votes = 
    winner = 

    print(f"Election Results")
    print(f"Total Votes: {int(total_votes)}")
    print
    print(f"Winner: {str(winner)}")