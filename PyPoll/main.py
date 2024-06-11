import os
import csv

# Define the path to the CSV file
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    header = next(csvreader)
    
    # Process the data
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        
        # Get the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate has other votes, add a vote to their count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # Otherwise, add the candidate to the dictionary and set their vote count to 1
        else:
            candidate_votes[candidate_name] = 1

# Calculate the percentage of votes each candidate won
for candidate_name in candidate_votes:
    candidates.append(candidate_name)
    votes = candidate_votes[candidate_name]
    percentage = (votes / total_votes) * 100
    candidate_votes[candidate_name] = {"percentage": percentage, "votes": votes}

# Determine the winner of the election
winner = max(candidate_votes, key=lambda k: candidate_votes[k]["votes"])

# Print the analysis
analysis = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate_name, data in candidate_votes.items():
    analysis += f"{candidate_name}: {data['percentage']:.3f}% ({data['votes']})\n"
analysis += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

print(analysis)

# Save the analysis to a text file
output_path = os.path.join("analysis", "results.txt")
os.makedirs("analysis", exist_ok=True)
with open(output_path, "w") as txtfile:
    txtfile.write(analysis)

