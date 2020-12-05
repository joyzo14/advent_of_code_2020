
def solve(input):
    seatIDs = []

    for line in input.splitlines():
        start = 0
        end = 127
        startColumn = 0
        endColumn = 7
        for letter in line:
            if letter == "F":
                end = end - int((end - start) / 2) - 1
            if letter == "B":
                start = start + int((end - start) / 2) + 1
            if letter == "L":
                endColumn = endColumn - int((endColumn - startColumn) / 2) - 1
            if letter == "R":
                startColumn = startColumn + int((endColumn - startColumn) / 2) + 1
        seatIDs.append(start * 8 + startColumn)

    seatIDs.sort()

    for i in range(0, len(seatIDs) - 1):
        if (seatIDs[i+1] - seatIDs[i] != 1):
            print(seatIDs[i] + 1)

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()