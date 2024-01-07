"""
    Question Link: https://adventofcode.com/2023/day/15
    CONSTRAINT: initialization sequence should be in one line only

    We have to create the hash function which does below work:
    for each string of the input
    1.Determine the ASCII code for the current character of the string.
    2.Increase the current value by the ASCII code you just determined.
    3.Set the current value to itself multiplied by 17.
    4.Set the current value to the remainder of dividing itself by 256.

"""

try:
    # Reading the input from the txt file or harcode in this code itself.
    # line ="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    with open("Lens-Library.txt") as file:
        line = file.readline().strip()

    # hash function as described in above description
    def hashFunction(str):
        stringHash = 0
        for char in str:
            stringHash += ord(char)
            stringHash *= 17
            stringHash %= 256
        return stringHash


    stringList = line.split(",") # Split the input line by , to get the strings

    ans = 0 # variable to store the final sum of each string which are part of initialization sequence
    for str in stringList:
        hashValueOfStr = hashFunction(str)
        ans += hashValueOfStr

    print("The sum of the results for each string in initialization sequence is =>",ans)
except Exception as e:
    print("Something went wrong while performing action, check the error/exception here=>",e)