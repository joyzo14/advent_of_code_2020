import re

def solve(input):

    input = input.splitlines()
    numberOfLines = len(input)
    preamble = 25
    found = False

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
            return

        found = False


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()