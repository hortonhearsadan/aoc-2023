import time

from loguru import logger

from aoc_2023 import day1, day2, day4, day6


def main():
    logger.info("Starting AOC 2023")
    timeit(day1.run)
    timeit(day2.run)
    timeit(day4.run)
    timeit(day6.run)


def timeit(fn):
    t = time.time()
    fn()
    logger.info(f"{fn.__module__} took {(time.time() - t) * 1000}ms")


if __name__ == "__main__":
    timeit(main)
