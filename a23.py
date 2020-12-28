import fileinput
from array import array


def main(inp):
    print("task1", task1(parse_input(inp)))
    print("task2", task2(parse_input(inp)))


def parse_input(inp):
    return list(map(int, inp[-1]))


def play(numbers, count):
    lowest = min(numbers)
    highest = max(numbers)
    # number -- index, value -- next
    links = array("I", [0] * (highest + 1))
    for i in range(1, len(numbers)):
        links[numbers[i - 1]] = numbers[i]
    links[numbers[-1]] = numbers[0]
    cur = numbers[0]
    for _ in range(count):
        a = links[cur]
        b = links[a]
        c = links[b]
        n = cur - 1
        n = highest if n < lowest else n
        while n in (a, b, c):
            n -= 1
            if n < lowest:
                n = highest
        t = links[c]
        links[c] = links[n]
        links[n] = a
        links[cur] = t
        cur = t

    return links


def task1(numbers):
    links = play(numbers, 100)
    n = links[1]
    res = ""
    while n != 1:
        res += str(n)
        n = links[n]
    return res


def task2(numbers):
    for i in range(max(numbers) + 1, 1000000 + 1):
        numbers.append(i)
    links = play(numbers, 10000000)
    return links[1] * links[links[1]]


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
