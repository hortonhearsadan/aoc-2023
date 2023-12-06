import math

from loguru import logger

from aoc_2023.utils import by_line, get_day_and_input


def part_1(data):
    times, dists = by_line(data)
    times = times.split()[1:]
    dists = dists.split()[1:]
    return quik_mafs(times, dists)


def quik_mafs(times, dists):
    total_ways = 1
    for t, d in zip(times, dists):
        a = -1
        b = int(t)
        c = -int(d)

        x = math.floor((-b + math.sqrt(b**2 - 4 * a * c)) / -2) + 1
        ways = b - (2 * x) + 1
        # logger.debug(ways)
        total_ways *= ways
    return total_ways


def part_2(data):
    times, dists = by_line(data)
    times = times.replace(" ", "").split(":")[1:]
    dists = dists.replace(" ", "").split(":")[1:]
    return quik_mafs(times, dists)


def run():
    d, f = get_day_and_input(__file__)

    logger.info(f"Starting Day {d}")
    part1 = part_1(f)
    logger.info(f"Part 1: {part1}")

    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")


def test_part_1():
    s = """Time:      7  15   30
Distance:  9  40  200"""

    assert part_1(s) == 288


def test_part_2():
    s = """Time:      7  15   30
Distance:  9  40  200"""

    assert part_2(s) == 71503
