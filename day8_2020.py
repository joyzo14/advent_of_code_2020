import re

def solve(input):
    index = 0
    accumulator = 0
    lines = input.splitlines()
    listOfIndexes = []
    numberOfLines = 0

    for line in lines:
        numberOfLines += 1

    while True:
        instructionPerLine = re.search('(^.{0,3}) ([-/+])(\d*)', lines[index])
        instruction = instructionPerLine.group(1)
        sign = instructionPerLine.group(2)
        value = int(instructionPerLine.group(3))

        listOfIndexes.append(index);

        if (instruction == "acc"):
            #solving acc instruciton
            if (sign == "+"):
                accumulator += value
            elif (sign == "-"):
                accumulator -= value

            index += 1
            print("new sum of accumulation after acc is " + str(accumulator))
            print("new index after acc is " + str(index))

        if (instruction == "jmp"):
            # solving jmp instruciton
            print("I am in JMP")
            print("value is "+ str(value))
            if (sign == "+"):
                index += int(value)

            elif (sign == "-"):
                index = index + (numberOfLines - value)
            print("new index after jmp is " + str(index))

        if (instruction == "nop"):
            # solving nop instruction
            print("I am in NOP")
            index += 1
            print("new index after nop " + str(index))

        # because index could be out of range
        index = index % numberOfLines
        print("new index after correction is " + str(index))
        print()

        if index in listOfIndexes:
            print("Sum of values in accumulator is " + str(accumulator))
            return

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()