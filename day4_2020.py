import re

def solve(input):
    # empty line would be splitting on two newline characters
    allPassports = input.split("\n\n")

    count = 0

    for passport in allPassports:
        if (("byr:" in passport) & ("iyr:" in passport) & ("eyr:" in passport) & ("hgt:" in passport) & ("hcl:" in passport) & ("ecl:" in passport) & ("pid:" in passport)):
            count += 1
            
    print(count)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()