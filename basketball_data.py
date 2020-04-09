# File:    hw2.py
# Author:  Ashar Nadeem
# Date:    09/27/2018
# Section: CMSC 331
# E-mail:  anadeem1@umbc.edu    

DATE = 0
MATCH = 1
SHOT_DISTANCE = 2
PLAYER = 3
RESULT = 4

def main():

    # User inputs the name of the file to load in
    filename = input("\nFile Name: ")

    fileObj = open(filename)    # Opens the file
    lines = fileObj.readlines() # Reads in the file
    fileObj.close()             # Closes the file

    # Creates a list 
    resultList = []
    index = 1

    # Variables needed to keep track of the total records and used records
    totalRecords = 0
    calculatedRecords = 0

    # Variables needed to keep track of error counts
    indexErrorsCount = 0
    valueErrorsCount = 0
    divideZeroErrrosCount = 0

    # Variables needed for calculation
    totalDistance = 0
    averageDistance = 0
    madeShots = 0

    # Loop throught the list 
    while index < len(lines):

        # Splits lines at the comma to read in each part seperately 
        line = lines[index].strip().split(",")

        # Try to take in each part of the line and turn into appropriate data type
        try:

            # Reads in each line and assigns it a variable
            date = str(line[DATE])
            match = str(line[MATCH])
            stringDistance = str(line[SHOT_DISTANCE])
            player = str(line[PLAYER])
            result = int(line[RESULT])

            # Converting the distance to a float (in case of blank spaces)
            distance = float(stringDistance)
            
            # add to records if result is 1                                                   
            if result == 1:
                calculatedRecords += 1
                madeShots += 1
                totalDistance += distance

        # What to do in the case of an index error for the result
        except IndexError:
            indexErrorsCount += 1
                        
        # What to do in the case of a value error for the result
        except ValueError:
            valueErrorsCount += 1
            
        # What to do in the case of a zero division error for the result
        except ZeroDivisionError:
            divideZeroErrrosCount += 1

        # Final case of the exception statements
        finally:
            # Appends and increments to the next place
            resultList.append(line)
            index += 1
            totalRecords += 1

            
        # Validation in the case that no shots are made
        try:
            averageDistance = totalDistance/madeShots
            averageDistance = str(round(averageDistance,2))
        except:
            averageDistance = 0
            averageDistance = str(round(averageDistance,2))

            
    # Output
    print("\nTotal number of records: ", totalRecords)
    print("The numbers of records used for calculation: ", calculatedRecords)
    print("The average successful shot distance: ", averageDistance)
    print("Number of index errors: ", indexErrorsCount)
    print("Number of value errors: ", valueErrorsCount)
    print("Number of division by zero erros: ", divideZeroErrrosCount,"\n")
    
main()