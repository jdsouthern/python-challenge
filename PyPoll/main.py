#import modules needed
import os
import csv
#file path to csv
electionDataCSV = os.path.join("Resources", "election_data.csv")
#initialize variables
totalVotes = 0
candidates = []
candidateVotes = {}
#create IO wrapper
with open(electionDataCSV, 'r') as csvFile:
#create file reader
    csvReader = csv.reader(csvFile, delimiter = ',')
#store header
    header = next(csvReader)
#count all votes and votes for each candidate
#names stored in list, individual votes stored in dictionary 
    for row in csvReader:
        totalVotes += 1
        candidateName = row[2]
        if candidateName not in candidates:
            candidates.append(candidateName)
            candidateVotes[candidateName] = 1
        else:
            candidateVotes[candidateName] += 1
#calculate percentage of votes each candidate recieved and store in list
percentages = []
for candidate in candidates:
    percentage = (100 * candidateVotes[candidate]) / totalVotes
    percentages.append(percentage)
#formatted results output to terminal
print("Election Results\n")
print("---------------------\n")
print(f"Total Votes: {totalVotes}\n")
print("---------------------\n")
#display percentage and number of votes by candidate
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percentages[i]:.3f}% ({candidateVotes[candidates[i]]})\n") 
print("---------------------\n")
#find index of highest percentage of votes
maxPercentage = 0
for percentage in percentages:
    if percentage > maxPercentage:
        maxPercentage = percentage
winnerIndex = percentages.index(maxPercentage)
#display winner
print(f"Winner: {candidates[winnerIndex]}\n")
print("---------------------")