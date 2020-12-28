f = open('a1_input')
lines = f.readlines()
lines = [int(r.strip()) for r in lines]

for r1 in lines:
    for r2 in lines:
        for r3 in lines:
            if r3 > r2 > r1 and r1 + r2 + r3 == 2020:
                print(r1 * r2 * r3)
