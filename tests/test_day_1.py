from pathlib import Path

from solutions.day_1 import Day1


def test_part_1() -> None:
    test = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    solver = Day1(test)

    assert solver.part_1() == 142


def test_part_2() -> None:
    test = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    solver = Day1(test)

    assert solver.part_2() == 281
