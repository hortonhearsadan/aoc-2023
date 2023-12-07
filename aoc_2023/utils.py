from pathlib import Path


def get_day_and_input(f):
    day = Path(f).stem.replace("day", "")
    inputs = Path(f"inputs/day{day}.txt")
    with open(inputs) as file:
        string = file.read()

    return day, string


def by_line(s):
    return s.strip().split("\n")


def by_double_line(s):
    return s.strip().split("\n\n")
