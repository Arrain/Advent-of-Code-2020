"""
AOC2020 - day4
"""
import re

FILEPATH = "./day4.txt"

MAP = []

AREVAILD = 0

PARAMS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

EYECOLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
HAIR_REGEX = re.compile("^#[0-9a-f]{6}$")
PID_REGEX = re.compile("^[0-9]{9}$")

with open(FILEPATH) as fp:
    MAP = fp.readlines()

    # python counts the endline as a character; need to trim
    for i, line in enumerate(MAP):
        MAP[i] = line[0:-1]

    valids = {"byr": False, "iyr": False, "eyr": False,
              "hgt": False, "hcl": False, "ecl": False, "pid": False}

    for line in MAP:
        if len(line) == 0:
            print(valids)
            if all(v for v in valids.values()):
                AREVAILD += 1

            valids = {"byr": False, "iyr": False, "eyr": False,
                      "hgt": False, "hcl": False, "ecl": False, "pid": False}
        else:
            bits = line.split(" ")

            for bit in bits:
                b = bit.split(":")

                if b[0] == "byr" and 1920 <= int(b[1]) <= 2002:
                    valids[b[0]] = True

                elif b[0] == "iyr" and 2010 <= int(b[1]) <= 2020:
                    valids[b[0]] = True

                elif b[0] == "eyr" and 2020 <= int(b[1]) <= 2030:
                    valids[b[0]] = True

                elif b[0] == "hgt":
                    val = b[1]
                    if val[-2:] == "in" and val[0:-2].isdigit() and 59 <= int(val[0:-2]) <= 76:
                        valids[b[0]] = True
                    if val[-2:] == "cm" and val[0:-2].isdigit() and 150 <= int(val[0:-2]) <= 193:
                        valids[b[0]] = True

                elif b[0] == "hcl" and HAIR_REGEX.match(b[1]):
                    valids[b[0]] = True

                elif b[0] == "ecl" and any(v == b[1] for v in EYECOLORS):
                    valids[b[0]] = True

                elif b[0] == "pid" and PID_REGEX.match(b[1]):
                    valids[b[0]] = True

    print(AREVAILD)
