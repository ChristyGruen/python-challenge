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


    #read csv
with open(PyPollCSV) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
        #will print location of csvdata, not the data itself
    print(csvreader)
        #read header row and print
    csv_header = next(csvreader)
        #Loop to capture list of months NMonths, list of profitloss NPL, sum of total profit TotProfit, 
        # calculate and create list of Change in PL, caputre max and min change and month

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

        


       
        # NMonths.append(line[0])
        # NPL.append(line[1])
        # TotProfit = TotProfit + int(line[1])
        # CurrentPL = int(line[1])
        # CalcChange = CurrentPL-PrevPL
        # ChangePL.append(CalcChange)
        # TotChange = TotChange + CalcChange
        # PrevPL = int(line[1])
        # if CalcChange < MinChange:
        #     MinChange = CalcChange
        #     MinChangeMo = line[0]
        # if CalcChange > MaxChange:
        #     MaxChange = CalcChange 
        #     MaxChangeMo = line[0]
        #counter +=1


Winner = "someone" #need to figure out how to pull winner
    # print summary to terminal and text file

print (TotVotes)
print (Candidates)
print (NewCand)
print (CandVotes)


print("```text")
print ("Election Results")
print ("----------------------------")
#print (f"Total Votes: {len(TotVotes)}")
print ("----------------------------")
#don't know how to create list of candidates with percent and totals
print ("----------------------------")
# print(f"Winner: {Winner}")
print ("----------------------------")
print ('```')

#try writing per zip lesson
# OutputFile = os.path.join("PyBankOutput.csv")
# with open(OutputFile,"w",newline='') as datafile:
#     writer = csv.writer(datafile)
#     writer.writerow("```text")
#     writer.writerow("Financial Analysis")
#     writer.writerow("----------------------------")
#     writer.writerow(f"Total Months: {len(NMonths)}")
#     writer.writerow(f"Total: ${TotProfit}")
#     writer.writerow(f"Average Change: ${AveChange}")
#     writer.writerow(f"Greatest Increase in Profits: {MaxChangeMo} (${MaxChange})")
#     writer.writerow(f"Greatest Decrease in Profits: {MinChangeMo} (${MinChange})")
#     writer.writerow('```')

#try writing per https://www.pythontutorial.net/python-basics/python-write-text-file/
#"/n" newline character per https://www.adamsmith.haus/python/answers/how-to-write-to-a-file-in-python#:~:text=Use%20writelines()%20to%20write,be%20in%20a%20single%20line.
# OutputFile = os.path.join("PyBankOutput.txt")
# with open(OutputFile,"w") as datafile:
#     datafile.writelines("```text""\n")
#     datafile.writelines("Financial Analysis""\n")
#     datafile.writelines("----------------------------""\n")
#     datafile.writelines(f"Total Months: {len(NMonths)}""\n")
#     datafile.writelines(f"Total: ${TotProfit}""\n")
#     datafile.writelines(f"Average Change: ${AveChange}""\n")
#     datafile.writelines(f"Greatest Increase in Profits: {MaxChangeMo} (${MaxChange})""\n")
#     datafile.writelines(f"Greatest Decrease in Profits: {MinChangeMo} (${MinChange})""\n")
#     datafile.writelines('```'"\n")
