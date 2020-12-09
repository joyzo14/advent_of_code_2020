import re

# borrow it from https://bugsdb.com/_en/debug/940e5ba1b511445bd7824c7d2e397f6a
def nth_repl(s, sub, repl, nth):
    find = s.find(sub)
    # if find is not p1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != nth:
        # find + 1 means we start at the last match start index + 1
        find = s.find(sub, find + 1)
        i += 1
    # if i  is equal to nth we found nth matches so replace
    if i == nth:
        return s[:find]+repl+s[find + len(sub):]
    return s


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

            if (sign == "+"):
                accumulator += value
            elif (sign == "-"):
                accumulator -= value

            # checking, if it's index, when the program have to be terminated
            if index == (numberOfLines - 1):
                print("Your input is terminated after 'acc' instruction")
                print("Sum of values in accumulator is " + str(accumulator))
                return

            index += 1

        if (instruction == "jmp"):

            if (sign == "+"):
                index += int(value)

                # checking, if it's index, when the program have to be terminated, so when the index is out of range, program have to be terminated
                if index > (numberOfLines - 1):
                    print("Your input is terminated after 'jump' instruction")
                    print("Sum of values in accumulator is " + str(accumulator))
                    return


            elif (sign == "-"):
                index = index + (numberOfLines - value)

        if (instruction == "nop"):

            # checking, if it's index, when the program have to be terminated
            if index == (numberOfLines - 1):
                print("Your input is terminated after 'nop' instruction")
                print("Sum of values in accumulator is " + str(accumulator))
                return

            index += 1

        # because index could be out of range
        index = index % numberOfLines
        #print("new index after correction is " + str(index))
        #print()

        if index in listOfIndexes:
            return




def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()

        # count number of "jmp" occurences
        countOfJmp = fileinput.count("jmp")

        # count number of "nop" occurences
        countOfNop = fileinput.count("nop")

        # substitute every "jmp" occurence with "nop"
        for i in range (1, countOfJmp + 1):
            changedInput = nth_repl(fileinput, "jmp", "nop", i)
            solve (changedInput)

        # substitute every "nop" occurence with "jmp"
        for i in range (1, countOfNop + 1):
            changedInput = nth_repl(fileinput, "nop", "jmp", i)
            solve (changedInput)


if __name__ == '__main__':
    main()