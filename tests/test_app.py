from python_project import add, greet


def test_greet() -> None:
    assert greet("Kai") == "Hello, Kai!"


def test_add() -> None:
    assert add(2, 3) == 5
