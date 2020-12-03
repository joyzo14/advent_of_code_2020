import math

def solve(input):
    validPasswords = 0
    for line in input.splitlines():
        firstNumber, left = line.split('-')
        secondNumber, letterWithColon, password  = left.split(" ")
        letter = letterWithColon[:1]
        if((password[int(firstNumber)-1] == letter) != (password[int(secondNumber)-1] == letter)):
            validPasswords += 1
            print(firstNumber, secondNumber, password)

    print(validPasswords)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()