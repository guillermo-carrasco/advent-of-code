"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?


"""
from typing import List


class Day3:
    def __init__(self, schematic: List[str]):
        self.schematic = [line.strip() for line in schematic]
        self.rows = len(self.schematic)
        self.cols = len(self.schematic[0])

    def _has_adjacent_symbols(self, x, y) -> bool:
        directions = [
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
        ]
        for x_inc, y_inc in directions:
            if (0 <= x + x_inc < self.rows) and (0 <= y + y_inc < self.cols):
                adjacent = self.schematic[x + x_inc][y + y_inc]
                if not adjacent.isdigit() and adjacent != ".":
                    return True
        return False

    def part_1(self) -> int:
        parts_sum = 0
        for i in range(self.rows):
            curr_num = []
            is_part = False
            for j in range(self.cols):
                curr_pos = self.schematic[i][j]
                if curr_pos.isdigit():
                    # Check if there are adjacent symbols and append the digit to the curr_num
                    is_part = is_part or self._has_adjacent_symbols(i, j)
                    curr_num.append(curr_pos)
                else:
                    # If it's not a digit, check if we had a previous digit and add it to the sum
                    if curr_num and is_part:
                        parts_sum += int("".join(curr_num))
                    curr_num = []
                    is_part = False
            # Edge case: This is the end of the current row, and we were checking for a number
            if curr_num and is_part:
                parts_sum += int("".join(curr_num))

        return parts_sum

    def part_2(self) -> int:
        return 0
