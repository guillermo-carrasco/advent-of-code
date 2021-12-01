import pytest


@pytest.fixture(scope="function")
def day_1_input(tmp_path):
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
