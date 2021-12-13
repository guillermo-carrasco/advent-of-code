from solutions.day_4 import Day4


def test_part_1(day_4_input) -> None:
    solver = Day4(day_4_input)

    assert solver.part_1() == 4512


def test_part_2(day_4_input) -> None:
    solver = Day4(day_4_input)

    assert solver.part_2() == 1924
