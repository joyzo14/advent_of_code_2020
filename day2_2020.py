import math

def solve(input):
    validPasswords = 0
    for line in input.splitlines():
        firstNumber, left = line.split('-')
        secondNumber, letterWithColon, password  = left.split(" ")
        countOfLetterInPassword = password.count(letterWithColon[:1])
        if((countOfLetterInPassword >= int(firstNumber)) & (countOfLetterInPassword <= int(secondNumber))):
            validPasswords +=1

    print(validPasswords)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()