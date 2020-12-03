
def solve(input):
    index = 0
    allLines = input.splitlines()
    lengthOfLine = len(allLines[0])
    numberOfTrees = 0

    for i in range (1, len(allLines)):
        index = (index + 3) % lengthOfLine

        print("checking line" + str(allLines[i]) + " at index " + str(index))
        if (allLines[i][index] == "#"):
            print("found tree at index in line " + str(i) + " at index " + str(index))
            numberOfTrees +=1
        else:
            print("not found tree at index in line " + str(i) + " at index " + str(index))

    print("Number of trees is " + str(numberOfTrees))

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()