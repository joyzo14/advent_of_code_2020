
def solve(input):
    index = 0
    allLines = input.splitlines()
    lengthOfLine = len(allLines[0])
    numberOfTrees = 0
    treesMultiplication = 1 # because of you cannont multiplicate by 0
    slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))

    for pair in (slopes):
        for i in range (pair[1], len(allLines), pair[1]):
            index = (index + pair[0]) % lengthOfLine

            print("checking line" + str(allLines[i]) + " at index " + str(index))
            if (allLines[i][index] == "#"):
                print("found tree at index in line " + str(i) + " at index " + str(index))
                numberOfTrees +=1
            else:
                print("not found tree at index in line " + str(i) + " at index " + str(index))

        # rest index for new pair
        index = 0
        # multiplication of number of trees for every slope pair
        treesMultiplication *= numberOfTrees
        # reset number of trees before every slope pair
        numberOfTrees = 0

    print("Multiplicated number of trees is " + str(treesMultiplication))

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()