"""Advent of Code executor"""
import click

from solutions import day_1, day_2, day_3, day_4


@click.command()
@click.argument("day", type=int)
@click.argument("part", type=int)
def run(day: int, part: int) -> None:
    with open(f"data/day_{day}.txt", "r") as f:
        text = f.readlines()
    solver = getattr(globals()[f"day_{day}"], f"Day{day}")(text)
    print(getattr(solver, f"part_{part}")())


if __name__ == "__main__":
    run()
