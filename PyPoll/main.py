# Modules
import os
import csv

csvpath = os.path.join(os.path.dirname(__file__),"Resources","election_data.csv")

# Lists to store data
ballot_id = []
county = []
candidate = []

# With open as csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row
    csvheader = next(csvreader)
    csvlist = list(csvreader)

    #Define lists
    for row in csvlist:
        # Add Ballot ID
        ballot_id.append(row[0])   
        
        # Add County
        county.append(row[1])
        
        # Add Candidate
        candidate.append(row[2]) 

    # The total number of votes cast
    total_votes = len(ballot_id)

    # A complete list of candidates who received votes
    candidate_list = list(sorted(set(candidate)))

    # The total number of votes each candidate won
    stockham_votes = candidate.count(candidate_list[0])
    degette_votes = candidate.count(candidate_list[1])
    doane_votes = candidate.count(candidate_list[2])

    # The percentage of votes each candidate won
    stockham_percent = round((stockham_votes / total_votes)*100, 3)
    degette_percent = round((degette_votes / total_votes)*100, 3)
    doane_percent = round((doane_votes / total_votes)*100, 3)

    # The winner of the election based on popular vote
    vote_list = [stockham_votes, degette_votes, doane_votes]
    ziplist = dict(zip(candidate_list, vote_list))
    winner = max(ziplist, key=ziplist.get)

    # Print analysis to terminal
    print("Election Results")
    print("----------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------")
    print(f"{candidate_list[0]}: {stockham_percent}% ({stockham_votes})")
    print(f"{candidate_list[1]}: {degette_percent}% ({degette_votes})")
    print(f"{candidate_list[2]}: {doane_percent}% ({doane_votes})")
    print("----------------------")
    print(f"Winner: {winner}")
    print("----------------------")

# Export text file with the results
output_file = os.path.join(os.path.dirname(__file__),"Analysis","PyPoll Analysis.txt")

f = open(output_file, "w")
f.writelines(["Election Results" + "\n" + 
    "-------------------------------------" + "\n"
    "Total Votes: " + str(total_votes) + "\n"
    "-------------------------------------" + "\n"
    "Charles Casper Stockham: " + str(stockham_percent) + "% (" + str(stockham_votes) + ")" + "\n"
    "Diana DeGette: " + str(degette_percent) + "% (" + str(degette_votes) + ")" + "\n"   
    "Raymon Anthony Doane: " + str(doane_percent) + "% (" + str(doane_votes) + ")" + "\n"
    "-------------------------------------" + "\n"
    "Winner: " + str(winner) + "\n"
    "-------------------------------------" + "\n"])
f.close()