from collections import deque

from loguru import logger

from aoc_2023.utils import by_line, get_day_and_input


class Card:
    def __init__(self, c):
        self.c = c
        self.id = None
        self.winning = None
        self.numbers = None

        self.matches = None
        self.parse()

    def parse(self):
        card_id, cards = self.c.split(":")
        self.id = int(card_id.split()[-1])
        winning, other = cards.split("|")
        self.winning = set(int(i) for i in winning.split())
        self.numbers = set(int(i) for i in other.split())

        self.matches = len(self.winning & self.numbers)


def part_1(data):
    lines = by_line(data)
    points = 0
    for line in lines:
        card = Card(line)
        matches = card.matches
        if matches:
            points += 2 ** (matches - 1)
    return points


def part_2(data):
    lines = by_line(data)
    cards = [Card(line) for line in lines]
    card_map = {c.id: c for c in cards}
    scratched = 0
    won = deque(cards)

    while won:
        next_card = won.popleft()
        scratched += 1

        for n in range(next_card.matches):
            won.append(card_map[next_card.id + n + 1])

    return scratched


def run():
    d, f = get_day_and_input(__file__)

    logger.info(f"Starting Day {d}")
    part1 = part_1(f)
    logger.info(f"Part 1: {part1}")

    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")


def test_part_1():
    s = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    assert part_1(s) == 13


def test_part_2():
    s = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    assert part_2(s) == 30
