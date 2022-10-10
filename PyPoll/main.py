#PyPoll Homework Chris Gruenhagen
    #import libraries os, csv
import os
import csv

    # define file path
PyPollCSV = os.path.join("Resources","election_data.csv")

    #within read csv loop
    #Total number of votes cast
        #create a TotVotes counter
    #Complete list of candidates
        #Create a list of candidates
        #set variable to nonsense string, if list[2] != variable, append to list, if ==, nothing
    #Votes per candidate
        #create a list of votes per candidate - per "House_of_pies_bonus.py"
    
    #after read csv loop
    #create function to calculate percent votes?
    #create dictionary for each candidate with percentage votes, total votes?

    #print
    #Total Votes: TotVotes


    #lists to store data, starting variables
TotVotes = 0
Candidates =[]
NewCand = "Chris Gruenhagen"
CandVotes = []
PercentVotes = []

    #read csv
with open(PyPollCSV) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')

        #read header row
    csv_header = next(csvreader)
        #Loop to capture csv info 
       
    #counter = 0
    for line in csvreader:
        TotVotes += 1
            #candidate list is not ordered by candidate, lists each candidate 3x
        # if line[2] != NewCand:
        #     NewCand = line[2]
        #     Candidates.append(line[2])
        #     CandVotes.append(0)
            #only add unique values to python list https://bobbyhadz.com/blog/python-only-add-unique-values-to-list
        if line[2] not in Candidates:
            NewCand = line[2]
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
 
#create zip for summary print, incorrect format when printed
# roster = zip(Candidates,PercentVotes,CandVotes)
# for r in roster:
#     print (r)

    # print summary to terminal and text file

# print (TotVotes)
# print (Candidates)
# print (NewCand)
# print (CandVotes)
# print (CurrentCand)
# print (CurrentCandIndex)
# print (PercentVotes)
# print (MaxVotes)
# print (MaxVotesIndex)
# print (Winner)

print("```text")
print ("Election Results")
print ("----------------------------")
print (f"Total Votes: {TotVotes}")
print ("----------------------------")
for i in range(0,len(Candidates)):
    print (f"{Candidates[i]}: {PercentVotes[i]}% ({CandVotes[i]})")
print ("----------------------------")
print(f"Winner: {Winner}")
print ("----------------------------")
print ('```')

# try writing per https://www.pythontutorial.net/python-basics/python-write-text-file/
# "/n" newline character per https://www.adamsmith.haus/python/answers/how-to-write-to-a-file-in-python#:~:text=Use%20writelines()%20to%20write,be%20in%20a%20single%20line.
OutputFile = os.path.join("analysis","PyPollOutput.txt")
with open(OutputFile,"w") as datafile:
    datafile.writelines("```text""\n")
    datafile.writelines("Election Results""\n")
    datafile.writelines("----------------------------""\n")
    datafile.writelines(f"Total Votes: {TotVotes}""\n")
    datafile.writelines("----------------------------""\n")
    for i in range(0,len(Candidates)):
        datafile.writelines(f"{Candidates[i]}: {PercentVotes[i]}% ({CandVotes[i]})""\n")
    datafile.writelines("----------------------------""\n")
    datafile.writelines(f"Winner: {Winner}""\n")
    datafile.writelines("----------------------------""\n")
    datafile.writelines('```'"\n")
