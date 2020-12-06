
def solve(input):

    groups = input.split("\n\n")
    sumOfCounts = 0

    for group in groups:
        sumOfCounts += len(set(group.replace("\n", "")))

    print(sumOfCounts)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()