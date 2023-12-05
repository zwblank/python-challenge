import os, csv

# --------------------------------------------------------------------------
# Opened the csv file and defined it as the 'election_file' variable. 
# Read through the csv data and stored the data within the 'election_data' variable. 
# --------------------------------------------------------------------------

election_file_path = os.path.join("PyPoll/Resources/election_data.csv")

with open(election_file_path) as election_file:
    election_data = csv.reader(election_file)


# --------------------------------------------------------------------------
# Skipped the header of the csv file to ensure clean data and got the total amount of votes cast by creating a list based on election_data.
# --------------------------------------------------------------------------

    next(election_data)
    vote_data = list(election_data)
    vote_count = len(vote_data)


# --------------------------------------------------------------------------
# Set the range the same length as vote_count to ensure all possible candidates are counted. 
# Looked through the 3rd column of the csv for candidate names. If a name wasn't already within the 'candidate_list' list, this added it in.
# Set the length of the 'candidate_list' as the amount of candidates.
# --------------------------------------------------------------------------

    candidate_list = []
    tally = []
    for x in range (0,vote_count):
        candidate = vote_data[x][2]
        tally.append(candidate)
        if candidate not in candidate_list: 
            candidate_list.append(candidate)
    candicount = len(candidate_list)


# --------------------------------------------------------------------------
# Created a list for votes and another for percentage of votes.
# Got amount of votes per candidate by counting how many times the name appeared within 'candidate_list'.
# Got percentage of votes dividing the candidate votes by total amount of votes.
# --------------------------------------------------------------------------

    votes = []
    percentage =[]
    for y in range (0,candicount):
        name = candidate_list[y]
        votes.append(tally.count(name))
        vote_percent = votes[y]/vote_count
        percentage.append(vote_percent)


# --------------------------------------------------------------------------
# Getting winner by looking for the most amount of votes
# --------------------------------------------------------------------------

    winner = votes.index(max(votes))  


# --------------------------------------------------------------------------
# Printing out election results to the terminal
# --------------------------------------------------------------------------

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {vote_count:,}")
    print("----------------------------")
    # Looped through the candidate data to grab the name, vote percentage, and amount of votes
    for z in range (0,candicount): 
        print(f"{candidate_list[z]}: {percentage[z]:.3%} ({votes[z]:,})")
    print("----------------------------")
    print(f"Winner: {candidate_list[winner]}")
    print("----------------------------")


# --------------------------------------------------------------------------
# Created a text file for the results.
# --------------------------------------------------------------------------

results = os.path.join("PyPoll/Analysis/election_results.csv")
with open(results,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {vote_count:,}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    for z in range (0,candicount): 
        file.write(f"{candidate_list[z]}: {percentage[z]:.3%} ({votes[z]:,})""\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {candidate_list[winner]}")
    file.write("\n")
    file.write("----------------------------")