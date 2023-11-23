import csv

def main():

    # create a list for headers and column spaces
    # headers = ["ID","LAST","FIRST","P1","P2","P3","CHALLENGES","FINAL MARK"]
    colSpaces = [12,20,20,6,6,6,15,0]

    infile = open("dataset1.csv","r")
    
    csvReader = csv.reader(infile) # construct the reader object and wire it up to the file

    gradeData = []

    # gradeData.append(headers) # append the header so that it will be printed 1st

    for row in csvReader:  # append the rows of csvReader
        gradeData.append(row)
    
    # these loops will print the 2d list
    for row in range(0,len(gradeData)): 
        # if (row > 0): # add % in the contents of last column but start in the 2nd row        
        #     gradeData[row][7] = gradeData[row][7] + "%"
        
        for col in range(0,len(gradeData[0])): 
            print(f"{gradeData[row][col]:<{colSpaces[col]}s}", end='') # print the output, change the end character to '' to remove newline in each loop 
        
        print('') # print an empty line to separate the rows

    infile.close()
    

main()