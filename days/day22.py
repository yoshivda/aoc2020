from lib import load_input


def solve(data):
    # return part_one(data.split("\n\n"))
    return part_two(data.split("\n\n"))


def part_one(data):
    players = [[int(card) for card in block.splitlines()[1:]] for block in data]
    winner = do_round(players)
    return sum((i + 1) * card for i, card in enumerate(players[winner][::-1]))


def part_two(data):
    players = [[int(card) for card in block.splitlines()[1:]] for block in data]
    winner = do_round(players, recurse=True)
    return sum((i + 1) * card for i, card in enumerate(players[winner][::-1]))


def do_round(players, recurse=False):
    states = set()
    while not any(len(cards) == 0 for cards in players):
        if tuple(tuple(cards) for cards in players) in states:
            return 0
        states.add(tuple(tuple(cards) for cards in players))
        top_cards = [cards.pop(0) for cards in players]
        if not recurse or any(len(players[i]) < top_cards[i] for i in range(len(players))):
            winner = top_cards.index(max(top_cards))
        elif recurse:
            winner = do_round([[players[i][c] for c in range(top_cards[i])] for i in range(len(players))])
        players[winner].append(top_cards.pop(winner))
        players[winner].append(top_cards[0])
    return winner


if __name__ == "__main__":
    print(solve(load_input(22, "small")))
    print(solve(load_input(22)))
