import fileinput


def main(inp):
    print("task1", task1(parse_input(inp)))
    print("task2", task2(parse_input(inp)))


def parse_input(inp):
    g = iter(inp)
    player1 = []
    player2 = []
    next(g)
    for c in g:
        if c == "":
            break
        player1.append(int(c))
    next(g)
    for c in g:
        if c == "":
            break
        player2.append(int(c))
    return player1, player2


def task1(game):
    player1, player2 = game
    while player1 and player2:
        c1, *player1 = player1
        c2, *player2 = player2
        if c1 > c2:
            player1.extend([c1, c2])
        else:
            player2.extend([c2, c1])

    win_deck = player1 or player2
    s = 0
    for i, c in enumerate(win_deck[::-1]):
        s += (i + 1) * c
    return s


def task2(game):
    player1, player2 = game

    def play(player1, player2):
        prev_states = set([])
        while player1 and player2:
            prev_states.add((tuple(player1), tuple(player2)))

            c1, *player1 = player1
            c2, *player2 = player2
            win1 = c1 > c2
            if c1 <= len(player1) and c2 <= len(player2):
                res1, res2 = play(player1[:c1], player2[:c2])
                win1 = bool(res1)

            if win1:
                player1.extend([c1, c2])
            else:
                player2.extend([c2, c1])

            if (tuple(player1), tuple(player2)) in prev_states:
                return player1, []

        return player1, player2

    player1, player2 = play(player1, player2)
    win_deck = player1 or player2
    s = 0
    for i, c in enumerate(win_deck[::-1]):
        s += (i + 1) * c
    return s


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
