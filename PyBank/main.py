from os import terminal_size

    #import libraries os, csv
import os
import csv

    # define file path
PyBankCSV = os.path.join("Resources","budget_data.csv")

    #lists to store data, starting variables
NMonths = []
NPL =[]
ChangePL = []
TotProfit = 0
TotChange = 0
MinChange = 0
MaxChange = 0

    #read csv
with open(PyBankCSV) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
        #will print location of csvdata, not the data itself
    #print(csvreader)
        #read header row
    csv_header = next(csvreader)
        #Loop to capture list of months NMonths, list of profitloss NPL, sum of total profit TotProfit, 
        # calculate and create list of Change in PL, caputre max and min change and month

    counter = 0
    for line in csvreader:
        if counter ==0:
            PrevPL = int(line[1])
        NMonths.append(line[0])
        NPL.append(line[1])
        TotProfit = TotProfit + int(line[1])
        CurrentPL = int(line[1])
        CalcChange = CurrentPL-PrevPL
        ChangePL.append(CalcChange)
        TotChange = TotChange + CalcChange
        PrevPL = int(line[1])
        if CalcChange < MinChange:
            MinChange = CalcChange
            MinChangeMo = line[0]
        if CalcChange > MaxChange:
            MaxChange = CalcChange 
            MaxChangeMo = line[0]
        counter +=1
    #average change calculated to correct for zero in ChangePL[0] for len(changePL)
AveChange = round(TotChange/(len(ChangePL)-1),2)

    # print summary to terminal and text file
#print(ChangePL)
print("```text")
print ("Financial Analysis")
print ("----------------------------")
print (f"Total Months: {len(NMonths)}")
print (f"Total: ${TotProfit}")
print (f"Average Change: ${AveChange}")
print (f"Greatest Increase in Profits: {MaxChangeMo} (${MaxChange})")
print (f"Greatest Decrease in Profits: {MinChangeMo} (${MinChange})")
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
OutputFile = os.path.join("PyBankOutput.txt")
with open(OutputFile,"w") as datafile:
    datafile.writelines("```text""\n")
    datafile.writelines("Financial Analysis""\n")
    datafile.writelines("----------------------------""\n")
    datafile.writelines(f"Total Months: {len(NMonths)}""\n")
    datafile.writelines(f"Total: ${TotProfit}""\n")
    datafile.writelines(f"Average Change: ${AveChange}""\n")
    datafile.writelines(f"Greatest Increase in Profits: {MaxChangeMo} (${MaxChange})""\n")
    datafile.writelines(f"Greatest Decrease in Profits: {MinChangeMo} (${MinChange})""\n")
    datafile.writelines('```'"\n")
