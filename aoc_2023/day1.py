import polars as pl
from loguru import logger
from polars import DataFrame

from aoc_2023.utils import by_line, get_day_and_input

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part_1(data):
    count = 0
    lines = by_line(data)
    for line in lines:
        code = ""
        for letter in line:
            if letter.isdigit():
                code += letter
                break
        for letter in line[::-1]:
            if letter.isdigit():
                code += letter
                break
        count += int(code)
    return count


def part_1_polars(data):
    return (
        DataFrame(pl.Series("line", by_line(data)))
        .with_columns(
            pl.col("line")
            .str.split("")
            .list.eval(pl.element().cast(pl.Int8, strict=False))
            .list.drop_nulls()
            .alias("numbers")
        )
        .with_columns(((pl.col("numbers").list.first() * 10) + pl.col("numbers").list.last()).alias("code"))
        .select(pl.col("code").sum())
        .row(0)[0]
    )


def part_2(data):
    count = 0
    lines = by_line(data)
    for line in lines:
        code = ""
        for i, letter in enumerate(line):
            if letter.isdigit():
                code += letter
                break
            num = line[i : i + 3]
            if num in numbers:
                code += numbers[num]
                break
            num = line[i : i + 4]
            if num in numbers:
                code += numbers[num]
                break

            num = line[i : i + 5]
            if num in numbers:
                code += numbers[num]
                break
        line2 = line[::-1]
        for i, letter in enumerate(line2):
            if letter.isdigit():
                code += letter
                break
            num = line2[i : i + 3][::-1]
            if num in numbers:
                code += numbers[num]
                break
            num = line2[i : i + 4][::-1]
            if num in numbers:
                code += numbers[num]
                break

            num = line2[i : i + 5][::-1]
            if num in numbers:
                code += numbers[num]
                break
        # logger.debug(code)
        count += int(code)
    return count


def run():
    d, f = get_day_and_input(__file__)

    logger.info(f"Starting Day {d}")
    part1 = part_1_polars(f)
    logger.info(f"Part 1: {part1}")

    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")


def test_part_1():
    s = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""

    assert part_1_polars(s) == 142


def test_part_2():
    s = """two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"""

    assert part_2(s) == 281
