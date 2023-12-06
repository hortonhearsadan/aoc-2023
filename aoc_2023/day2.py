from loguru import logger

from aoc_2023.utils import by_line, get_day_and_input


class Pick:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue


class Bag(Pick):
    def can_pick(self, pick):
        if self.red >= pick.red and self.blue >= pick.blue and self.green >= pick.green:
            return True
        return False

    def power(self):
        return self.red * self.green * self.blue


class Game:
    def __init__(self, game_string):
        self.id = None
        self.picks = None
        self.raw = game_string
        self.parse_game()

    def parse_game(self):
        game, picks = self.raw.split(":")
        self.id = int(game.split(" ")[-1])

        picks = picks.split(";")
        self.picks = []
        for pick in picks:
            colours = pick.split(",")
            p = {}
            for colour in colours:
                n, c = colour.strip().split(" ")
                p[c] = int(n)
            self.picks.append(Pick(**p))

    @property
    def max_red(self):
        return max(p.red for p in self.picks)

    @property
    def max_green(self):
        return max(p.green for p in self.picks)

    @property
    def max_blue(self):
        return max(p.blue for p in self.picks)


def parse_games(lines):
    games = []
    for game in lines:
        g = Game(game)
        g.parse_game()
        games.append(g)
    return games


def part_1(data, b):
    lines = by_line(data)
    games = parse_games(lines)

    bag = Bag(*b)
    valid_games = []
    for game in games:
        for pick in game.picks:
            if not bag.can_pick(pick):
                break
        else:
            valid_games.append(game.id)
            continue

    return sum(valid_games)


def part_2(data):
    lines = by_line(data)
    games = parse_games(lines)

    powers = []
    for game in games:
        bag = Bag(game.max_red, game.max_green, game.max_blue)
        powers.append(bag.power())
    return sum(powers)


def run():
    d, f = get_day_and_input(__file__)

    logger.info(f"Starting Day {d}")
    part1 = part_1(f, (12, 13, 14))
    logger.info(f"Part 1: {part1}")

    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")


def test_part_1():
    s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    bag = (12, 13, 14)
    assert part_1(s, bag) == 8


def test_part_2():
    s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    assert part_2(s) == 2286
