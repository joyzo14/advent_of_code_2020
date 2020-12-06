
def solve(input):

    groups = input.split("\n\n")
    sumOfCounts = 0

    for group in groups:
        # split every group into lines
        linesInGroup = group.splitlines()

        # map every line of group into set
        mappedLinesInSets = list(map(lambda line: set(line), linesInGroup))

        # count of intersection of all sets in one group
        countOfIntersection = len(mappedLinesInSets[0].intersection(*mappedLinesInSets))

        # add counf of intersection into sum of all intersections
        sumOfCounts += countOfIntersection

    print(sumOfCounts)

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()