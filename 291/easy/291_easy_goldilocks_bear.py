from pathlib import Path

with open(Path(__file__).with_name("input")) as inputfile:
    w, t = [int(i) for i in inputfile.readline().split()]
    print(
        [
            idx
            for idx, line in enumerate(inputfile.readlines(), 1)
            if int(line.split()[0]) >= w and int(line.split()[1]) <= t
        ]
    )
