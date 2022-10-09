from os import terminal_size



    # import libraries os, csv
import os
import csv

    # define file path
PyBankCSV = os.path.join("Resources","budget_data.csv")

    #lists to store data, starting variables
NMonths = []
NPL =[]
ChangePL = []
TotProfit = 0
LineCounter = 0

    #read csv
with open(PyBankCSV) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
        #will print location of csvdata, not the data itself
    print(csvreader)
        #read header row and print
    csv_header = next(csvreader)
    print(f"DON'T KEEP FOR FINAL HOMEWORKK CSV Header: {csv_header}")

    counter = 0
    for line in csvreader:
        #if counter ==0:
            #PrevPL = int(line[1])

    #Total number of months
        # NMonths = loop to create list of months and count list length
        # NPL= loop to create list of profit/loss (just in case)
        # ChangePL = loop to calculate change by month
        NMonths.append(line[0])
        NPL.append(line[1])
        #CurrentPL = int(line[1])
        #Christry = PrevPL - CurrentPL
        #ChangePL.append(Christry)
        PrevPL = line[1]

    #Net total of Profit 
        # TotProfit =  loop to add profit/loss to total profit counter
        #TotProfit = TotProfit + line[1]

print (NMonths)
print (len(NMonths))

print ('++++++++')
#print (ChangePL)
    #Profit/losses change 


    
    #greatest increase in profits
        # MaxPL = max profit loss change list value and month
        # max ChangePL, return index, use index to find month in NMonths
    #greatest decrease in profits
        # MinPL = min profit loss change list value and month
        # min ChangePL, return index, use index to find month in NMonths
    # print summary to terminal and text file
        # print header "Financial Analysis"
        # print separator "-------"
        # print with titles: NMonths, TotProfit, AvePL, MaxPL, MinPL
   

#
