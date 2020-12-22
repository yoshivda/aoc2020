from lib import load_input


def solve(data):
    # return play_game(data.split("\n\n"), 1)
    return play_game(data.split("\n\n"), 2)


def play_game(data, part):
    players = [[int(card) for card in block.splitlines()[1:]] for block in data]
    winner = play_round(players, part == 2)
    return sum((i + 1) * card for i, card in enumerate(players[winner][::-1]))


def play_round(players, recurse=False):
    states = set()
    while not any(len(cards) == 0 for cards in players):
        if tuple(tuple(cards) for cards in players) in states:
            return 0
        states.add(tuple(tuple(cards) for cards in players))
        top_cards = [cards.pop(0) for cards in players]
        if not recurse or any(len(players[i]) < top_cards[i] for i in range(len(players))):
            winner = top_cards.index(max(top_cards))
        else:
            winner = play_round([[players[i][c] for c in range(top_cards[i])] for i in range(len(players))])
        players[winner].append(top_cards.pop(winner))
        players[winner].append(top_cards[0])
    return winner


if __name__ == "__main__":
    print(solve(load_input(22, "small")))
    print(solve(load_input(22)))
