from pathlib import Path

from solutions.day_1 import Day1


def test_part_1(day_1_input: Path) -> None:
    solver = Day1(day_1_input)

    assert solver.part_1() == 7


def test_part_2(day_1_input: Path) -> None:
    solver = Day1(day_1_input)

    assert solver.part_2() == 5
