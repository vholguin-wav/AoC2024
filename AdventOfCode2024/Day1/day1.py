# Advent of Code 2024 - Day 1
# Vincent Holguin - Mar 2025
# Given 2 lists, pair each i element of each list, and find the difference.
# Finally, add up the differences between every i element for your total
# distance.

# First we need to find how the lists are input. Appears to be tab seperated.
# Left side of text file is one list, right side is another.
# Just checked, its not a tab but rather 3 space characters.


# For reading from our file
import os

# Will use this to test my function splits the 'string' properly
testData = ("100   200\n"
            "300   400\n"
            "500   600"
            )

# Will need to read the data and use list comprehension to split into two lists

# Sort and find the difference between values in our two lists
def findDif(listOne, listTwo):
    counter = 0
    for i in range(len(listOne)):
        counter += abs(listOne[i] - listTwo[i])
    print(counter)

# Lists in as a string to function
def inputLists(listIn):
    listLeft = []
    listRight = []
    # Split at three spaces
    listSplit = [int(l.split(' ')[0]) for l in listIn.split()]
    # Get our two lists
    listLeft = listSplit[::2]
    listRight = listSplit[1::2]
    listLeft.sort()
    listRight.sort()
    findDif(listLeft,listRight)
    return None

# Read our puzzle text.
def getInput():
    fileIn = input("Enter filepath: ")
    try:
        with open(fileIn, 'r') as f:
            data = f.read()
            inputLists(data)
            return None
    except FileNotFoundError:
        print(f'File not found!')
        return None
    except Exception as e:
        print(f'Error {e} occurred')
        return None

# Main func
def main():
    # global testData
    # print(f'Test Data: {testData}')
    # inputLists(testData)
    # print(f'List 1: {listLeft}')
    # print(f'List 2: {listRight}')
    # findDif()
    getInput()

if __name__ == '__main__':
    main()
    
    
