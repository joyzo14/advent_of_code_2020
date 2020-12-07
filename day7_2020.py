import re

def solve(input):
    lines = input.splitlines()
    bagsContainShinyBag = ["shiny gold"]
    index = 0
    max = 0


    while True:
        for line in lines:
            # piece of line after word contains
            containsBags = re.search("(?<=contain).*$", line).group(0)

            # for every bag in match bags
            for bag in bagsContainShinyBag:
                if bag in containsBags:
                    firstBagInLine = re.search(".+?(?=bags)", line)
                    if firstBagInLine.group(0) not in bagsContainShinyBag:
                        bagsContainShinyBag.append(firstBagInLine.group(0))
        if max < len(bagsContainShinyBag):
            max = len(bagsContainShinyBag)
        else:
            break
    # substract 'shiny gold'
    print(max - 1)





def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()