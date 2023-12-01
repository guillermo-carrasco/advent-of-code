from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def day_1_input(tmp_path: Path) -> Path:
    p = tmp_path / "input.txt"
    content = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    p.write_text("\n".join(content))

    return p
