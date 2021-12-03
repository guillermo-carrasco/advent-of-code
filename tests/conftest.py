from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def day_1_input(tmp_path: Path) -> Path:
    p = tmp_path / "input.txt"
    content = [
        "199",
        "200",
        "208",
        "210",
        "200",
        "207",
        "240",
        "269",
        "260",
        "263",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_2_input(tmp_path: Path) -> Path:
    p = tmp_path / "input.txt"
    content = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_3_input(tmp_path: Path) -> Path:
    p = tmp_path / "input.txt"
    content = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    p.write_text("\n".join(content))

    return p
