"""Advent of Code executor"""
import click

from solutions import (
    day_1,
    day_2,
)


@click.command()
@click.argument("day", type=int)
@click.argument("part", type=int)
def run(day: int, part: int) -> None:
    solver = getattr(globals()[f"day_{day}"], f"Day{day}")(f"data/day_{day}.txt")
    print(getattr(solver, f"part_{part}")())


if __name__ == "__main__":
    run()
