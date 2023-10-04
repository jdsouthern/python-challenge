#import modules needed
import os
import csv
#set read filepath
budgetDataCSV = os.path.join("Resources", "budget_data.csv")
#create file wrapper
with open(budgetDataCSV, 'r') as csvFile:
    #create file reader
    csvReader = csv.reader(csvFile, delimiter=",")
    #file header as list
    header = next(csvReader)
    #file first row of data as list
    initials = next(csvReader)
    #initialize data collecting variables
    totalMonths = 1
    totalProfit = int(initials[1])
    previousRow = int(initials[1])
    changesList = []
    greatestIncrease = [initials[0], int(initials[1])]
    greatestDecrease = [initials[0], int(initials[1])]
    #loop through remainder of csv
    for row in csvReader:
        totalMonths += 1 #count total months
        totalProfit += int(row[1]) #calc total profit
        changeFromLast = int(row[1])-previousRow #calc monthly change
        changesList.append(changeFromLast) #store monthly change
        previousRow = int(row[1]) #update value
        if changeFromLast > greatestIncrease[1]: #find greatest increase
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = changeFromLast
        if changeFromLast < greatestDecrease[1]: #find greatest decrease
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = changeFromLast
#formatted terminal output      
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {totalMonths}\n")
print(f"Total: ${totalProfit}\n")
averageChange = sum(changesList) / len(changesList) #calc average monthly change
print(f"Average Change: ${averageChange:.2f}\n")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")
#IO wrapper and formatted txt output
analysisTXT = os.path.join("analysis", "PyBank Analysis.txt")
with open(analysisTXT, 'w') as txtFile:
     
    txtFile.write("Financial Analysis\n")
    txtFile.write("----------------------------\n")
    txtFile.write(f"Total Months: {totalMonths}\n")
    txtFile.write(f"Total: ${totalProfit}\n")
    txtFile.write(f"Average Change: ${averageChange:.2f}\n")
    txtFile.write(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n")
    txtFile.write(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")
