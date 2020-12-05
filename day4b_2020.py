import re

def solve(input):
    # empty line would be splitting on two newline characters
    allPassports = input.split("\n\n")

    count = 0

    for passport in allPassports:
        if (("byr:" in passport) & ("iyr:" in passport) & ("eyr:" in passport) & ("hgt:" in passport) & ("hcl:" in passport) & ("ecl:" in passport) & ("pid:" in passport)):
            byr = re.search('byr:(\d*)', passport)
            iyr = re.search('iyr:(\d*)', passport)
            eyr = re.search('eyr:(\d*)', passport)
            hgt = re.search('hgt:(\d*)(\w*)', passport)
            hcl = re.search('hcl:(#?[0-9a-f]*)', passport)
            ecl = re.search('ecl:(\w*)', passport)
            pid = re.search('pid:(\w*)', passport)

            if((int(byr.group(1)) >= 1920) & (int(byr.group(1)) <= 2002)):
                if ((int(iyr.group(1)) >= 2010) & (int(iyr.group(1)) <= 2020)):
                    if ((int(eyr.group(1)) >= 2020) & (int(eyr.group(1)) <= 2030)):
                        if(True if ((int(hgt.group(1)) >= 150) & (int(hgt.group(1)) <= 193) & (hgt.group(2) == "cm")) else False |
                            True if ((int(hgt.group(1)) >= 59) & (int(hgt.group(1)) <= 76) & (hgt.group(2) == "in")) else False):
                            if (len(hcl.group(1)) > 0):
                                if((hcl.group(1)[0] == "#") & (len(hcl.group(1)[1:]) == 6)):
                                    if(ecl.group(1) in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")):
                                        if(pid.group(1).isdigit() & (len(pid.group(1)) == 9)):
                                            print(pid.group(1))
                                            count += 1
    print(count)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()