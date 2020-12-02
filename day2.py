"""
AOC2020 - day2
"""

FILEPATH = "./day2.txt";

with open(FILEPATH) as fp:
    lines = fp.readlines();

    CNT1 = 0;
    CNT2 = 0;

    for line in lines:
        strBits = line.split(' ');
        lower = int(strBits[0].split('-')[0]);
        higher = int(strBits[0].split('-')[1]);
        theChar = strBits[1].split(':')[0];
        pwd = strBits[2];

        PCNT = 0;

        for i, c in enumerate(pwd):
            if c == theChar:
                PCNT += 1;

        if lower <= PCNT <= higher:
            CNT1 += 1;

        if ((pwd[lower-1] != theChar and pwd[higher-1] == theChar)
            or (pwd[lower-1] == theChar and pwd[higher-1] != theChar)):
            CNT2 += 1;

print(CNT1, CNT2);
