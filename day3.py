"""
AOC2020 - day3
"""

FILEPATH = "./day3.txt"

MAP = []
ROWLEN = 0


def doFall(down, right):
    cnt = 0

    myRight = 0

    for ind in range(down, len(MAP), down):
        myRight += right
        if myRight >= ROWLEN:
            myRight -= ROWLEN
        if MAP[ind][myRight] == '#':
            cnt += 1

    return cnt


with open(FILEPATH) as fp:
    MAP = fp.readlines()

    # python counts the endline as a character; need to trim
    for i, line in enumerate(MAP):
        MAP[i] = line[0:-1]

    ROWLEN = len(MAP[0])

    print(doFall(1, 1))
    print(doFall(1, 3))
    print(doFall(1, 5))
    print(doFall(1, 7))
    print(doFall(2, 1))
    print(doFall(1, 1) * doFall(1, 3) * doFall(1, 5)
          * doFall(1, 7) * doFall(2, 1))
