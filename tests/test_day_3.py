from solutions.day_3 import Day3


class TestDay3:
    input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    solver = Day3(input)

    def test_part_1(self) -> None:
        assert self.solver.part_1() == 4361

    def test_part_2(self) -> None:
        assert self.solver.part_2() == 0
