

def solve(input):

    input = input.splitlines()

    # creating 2 dimensional list with all positions
    for i in range(len(input)):
        input[i] = list(input[i])

    while (True):
        # coordinates for seats have to be occupied
        coordinatesForNewOccupied = []
        # coordinates for seats have to be deleted
        coordinatesForDeleteOccupied = []

        # counting adjacent occupied seats for each direction - (one of the eight positions immediately up, down, left, right, or diagonal from the seat)
        for i in range(len(input)):
            for j in range(len(input[i])):
                countOfOccupied = 0
                try:
                    if ((i-1>=0)&((input[i - 1][j]) == '#')):
                        countOfOccupied += 1
                except IndexError:
                    pass
                try:
                    if ((input[i + 1][j]) == '#'):
                        countOfOccupied += 1
                except IndexError:
                    pass
                try:
                    if ((j-1>=0)&((input[i][j - 1]) == '#')):
                        countOfOccupied += 1
                except IndexError:
                    pass
                try:
                    if ((input[i][j + 1]) == '#'):
                        countOfOccupied += 1
                except IndexError:
                    pass
                try:
                    if ((i-1>=0)&(j-1>=0)&((input[i - 1][j - 1]) == '#')):
                        countOfOccupied += 1
                except IndexError:
                    pass
                try:
                    if (input[i + 1][j + 1]) == '#':
                        countOfOccupied += 1
                except IndexError:
                    pass
                try:
                    if ((j-1>=0)&((input[i + 1][j - 1]) == '#')):
                        countOfOccupied += 1
                except IndexError:
                    pass
                try:
                    if ((i-1>=0)&((input[i - 1][j + 1]) == '#')):
                        countOfOccupied += 1
                except IndexError:
                    pass

                # checking conditions:
                # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                if (input[i][j])=="L":
                    if(countOfOccupied==0):
                        coordinatesForNewOccupied.append((i, j))
                # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                if (input[i][j]=="#"):
                    if (countOfOccupied) >= 4:
                        coordinatesForDeleteOccupied.append((i, j))

        # id does not exist new occupied or seats for deleting, then break
        if not coordinatesForNewOccupied:
            if not coordinatesForDeleteOccupied:
                break

        # change layout of seats - delete occupied seats or adding occupied
        for i in range(len(input)):
            for j in range(len(input[i])):
                if (i,j) in coordinatesForNewOccupied:
                    input[i][j]="#"
                if (i,j) in coordinatesForDeleteOccupied:
                    input[i][j]="L"

    # final count of occupied seats after the chaos is stabilized is
    count = 0
    for line in input:
        for i in line:
            if i == "#":
                count += 1;

    print("Number of occupied seats after the chaos is stabilized is: " + str(count))


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()