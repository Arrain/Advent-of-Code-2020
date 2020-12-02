"""
AOC2020 - day1
"""
import sys;

FILEPATH = "./day1.txt";

with open(FILEPATH) as fp:
    lines = fp.readlines();

    EXISTING = [];

    for line in lines:
        val = int(line);

        ## part 1
        # for i in EXISTING:
        #     if val + i == 2020:
        #         print(val * i);
        #         sys.exit();
        # EXISTING.append(val);

        for i, v1 in enumerate(EXISTING):
            for j, v2 in enumerate(EXISTING, i):
                if val + v1 + v2 == 2020:
                    print(val * v1 * v2);
                    sys.exit();

        EXISTING.append(val);
