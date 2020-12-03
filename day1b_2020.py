
def solve(input):
    for line in input.splitlines():
        for line2 in input.splitlines():
            for line3 in input.splitlines():
                #if sum is 2020, then print multiplication of this 3 numbers
                if((int(line) + int(line2) + int(line3)) == 2020):
                    print(int(line) * int(line2) * int(line3))
                    return

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()