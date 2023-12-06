from loguru import logger

from aoc_2023.utils import get_day_and_input


def part_1(data):
    pass


def part_2(data):
    pass


def run():
    d, f = get_day_and_input(__file__)

    logger.info(f"Starting Day {d}")
    part1 = part_1(f)
    logger.info(f"Part 1: {part1}")

    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")


def test_part_1():
    s = """"""

    assert part_1(s) == 142


def test_part_2():
    s = """"""

    assert part_2(s) == 281
