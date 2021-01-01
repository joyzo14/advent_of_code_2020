import re

def solve(input):

    input = input.splitlines()
    numberOfLines = len(input)
    preamble = 25
    found = False
    foundIndex = 0
    foundNumber = 0

    input = list(map(int, input))

    #checking every number
    for i in range(preamble, numberOfLines):
        #iterating 25 previous numbers
        for j in range (i - preamble, i):
            for k in range(i - preamble, i):
                #because it isn't allowed som of two same numbers
                if (j != k):
                    #if found sum of any two of the 25 immediately previous numbers
                    if (input[j] + input[k] == input[i]):
                        found = True
        #if not found sum of any two of the 25 immediately previous numbers
        if (found == False):
            print("First unvalid number is: " + str(input[i]))
            foundIndex = i
            foundNumber = input[i]
            break

        found = False

    #checking sum of sliced contiguos numbers between index 0 and index of first invalid number
    for i in range(foundIndex):
        for j in range(i + 1, foundIndex):
            if sum(input[i:j]) == foundNumber:
                print("Smallest number in this contiguous range is: " + str(min(input[i:j])))
                print("Largest number in this contiguous range is: " + str(max(input[i:j])))
                print ("Sum of these two numbers is: " + str(min(input[i:j]) + max(input[i:j])))
                return


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()