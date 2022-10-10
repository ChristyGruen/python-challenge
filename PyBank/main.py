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
    print(csvreader)
        #read header row and print
    csv_header = next(csvreader)
        #Loop to capture list of months NMonths, list of profitloss NPL, sum of total profit TotProfit, calculate and create list of Change in PL, 

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
    
AveChange = round(TotChange/(len(ChangePL)-1),2)

    #greatest increase in profits
        # MaxPL = max profit loss change list value and month
        # max ChangePL, return index, use index to find month in NMonths
    #greatest decrease in profits
        # MinPL = min profit loss change list value and month
        # min ChangePL, return index, use index to find month in NMonths
    # print summary to terminal and text file
print(ChangePL)
print("```text")
print ("Financial Analysis")
print ("----------------------------")
print (f"Total Months: {len(NMonths)}")
print (f"Total: ${TotProfit}")
#
print (f"Average Change: ${AveChange}")
print (f"Greatest Increase in Profits: {MaxChangeMo} (${MaxChange})")
print (f"Greatest Decrease in Profits: {MinChangeMo} (${MinChange})")
print ('```')

#
