def main():
    f = open("a2_input")

    count = 0
    count2 = 0
    lines = f.readlines()
    lines = [r.strip() for r in lines]
    for line in lines:
        args = line.split(": ")
        if check(*args):
            count += 1
        if check2(*args):
            count2 += 1

    print("valid count", count)
    print("valid count2", count2)


def check(policy, password):
    minmax, letter = policy.split(" ")
    min_o, max_o = minmax.split("-")
    min_o = int(min_o)
    max_o = int(max_o)
    return min_o <= password.count(letter) <= max_o


def check2(policy, password):
    pos, letter = policy.split(" ")
    fp, sp = pos.split("-")
    fp = int(fp) - 1
    sp = int(sp) - 1
    return (password[fp] == letter) ^ (password[sp] == letter)


if __name__ == "__main__":
    main()
