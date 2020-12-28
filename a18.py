import fileinput
import tokenize
from io import StringIO


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def calc_polish(polish):
    stack = []
    for t in polish:
        if t.type == tokenize.NUMBER:
            stack.append(t.string)
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(eval("{}{}{}".format(left, t.string, right)))
    return stack[-1]


def calc(expr, prior=False):
    stack1 = []
    stack2 = []
    last = None
    tokens = tokenize.generate_tokens(StringIO(expr).readline)
    while True:
        if last is None:
            last = next(tokens)
        if last.type in (tokenize.NEWLINE, tokenize.ENDMARKER):
            if stack2:
                stack1.append(stack2.pop())
                continue
            break
        assert last.type in (tokenize.NUMBER, tokenize.OP)

        if last.type == tokenize.NUMBER:
            stack1.append(last)
            last = None
            continue

        if (
            not stack2
            or last.string == "("
            or (stack2[-1].string == "(" and last.string != ")")
        ):
            stack2.append(last)
            last = None
            continue

        if last.string == ")":
            op = stack2.pop()
            if op.string == "(":
                last = None
            else:
                stack1.append(op)
            continue

        if prior:
            if last.string == "*" or last.string == stack2[-1]:
                stack1.append(stack2.pop())
            else:
                stack2.append(last)
                last = None
        else:
            stack1.append(stack2.pop())

    return calc_polish(stack1)


def task1(inp):
    s = 0
    for expr in inp:
        s += calc(expr)
    return s


def task2(inp):
    s = 0
    for expr in inp:
        s += calc(expr, True)
    return s


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
