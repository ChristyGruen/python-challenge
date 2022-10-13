#PyPoll Homework Chris Gruenhagen
 
import os
import csv

    # define file path
PyPollCSV = os.path.join("Resources","election_data.csv")

    #lists to store data, starting variables
TotVotes = 0
Candidates =[]
CandVotes = []
PercentVotes = []

    #read csv
with open(PyPollCSV) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')

        #read and store header row
    csv_header = next(csvreader)
        #Loop to capture csv info 
       
    #counter = 0
    for line in csvreader:
        TotVotes += 1
            #only add unique values to python list https://bobbyhadz.com/blog/python-only-add-unique-values-to-list
        if line[2] not in Candidates:
            Candidates.append(line[2])
            CandVotes.append(0)
            PercentVotes.append(0)
        CurrentCand = line[2]
        CurrentCandIndex = Candidates.index(CurrentCand)
        CandVotes[CurrentCandIndex] +=1
  
    #create percentage list
    for i in range(0,len(PercentVotes)):
        PercentVotes[i] =round((CandVotes[i]/TotVotes)*100,3)
      
    #Determine winner
    MaxVotes = CandVotes[0]
    for i in range(0,len(CandVotes)):
        if CandVotes[i] > MaxVotes:
            MaxVotes = CandVotes[i]
            MaxVotesIndex = CandVotes.index(MaxVotes)
            Winner = Candidates[MaxVotesIndex]
 
    # print summary to terminal and text file

print ("Election Results")
print ("----------------------------")
print (f"Total Votes: {TotVotes}")
print ("----------------------------")
for i in range(0,len(Candidates)):
    print (f"{Candidates[i]}: {PercentVotes[i]}% ({CandVotes[i]})")
print ("----------------------------")
print(f"Winner: {Winner}")
print ("----------------------------")


# write per https://www.pythontutorial.net/python-basics/python-write-text-file/ and use "/n" newline character.
OutputFile = os.path.join("analysis","PyPollOutput.txt")
with open(OutputFile,"w") as datafile:
 
    datafile.writelines("Election Results""\n")
    datafile.writelines("----------------------------""\n")
    datafile.writelines(f"Total Votes: {TotVotes}""\n")
    datafile.writelines("----------------------------""\n")
    for i in range(0,len(Candidates)):
        datafile.writelines(f"{Candidates[i]}: {PercentVotes[i]}% ({CandVotes[i]})""\n")
    datafile.writelines("----------------------------""\n")
    datafile.writelines(f"Winner: {Winner}""\n")
    datafile.writelines("----------------------------""\n")
 
