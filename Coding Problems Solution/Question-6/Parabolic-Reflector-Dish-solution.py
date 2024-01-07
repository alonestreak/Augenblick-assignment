"""
    Question Link: https://adventofcode.com/2023/day/14

    Two pointer approach 
    one pointer points to every row while we are interating over columns
    second pointer points to the row where we can move the stone 

"""

try:
    # Reading the input from the txt file
    with open("Parabolic-Reflector-Dish.txt") as file:
        fileData = file.read().strip().split("\n")

    totalRows,totalColumns=len(fileData),len(fileData[0])

    finalLoad=0         # final load on the beams

    # iterate over each column and for each row calculate the load based on the position of stone
    for column in range(totalColumns):
        """
            Initial load is equal to number of rows since the top row will have load factor of number of rows
            rowLoad is also equal to number of rows because to get the rounded rocks all roll north we have to start with top position
        """
        currentLoad,rowLoad=totalRows,totalRows

        # Iterate over the rows
        for row in range(totalRows):
            # if we encounter "O" then add the currentLoad to the final load and reduce the initial load by 1 
            if(fileData[row][column]=="O"):
                finalLoad+=currentLoad
                currentLoad-=1
            # If we encounter "#" then move the currentLoad to rowLoad -1 since this rock will not move
            elif(fileData[row][column]=="#"):
                currentLoad = rowLoad-1
            rowLoad-=1

    print(finalLoad)
except Exception as e:
    print("Something went wrong while performing action, check the error/exception here=>",e)