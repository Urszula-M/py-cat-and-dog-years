from app.main import get_human_age


def test_should_return_zero_for_ages_about_first_step() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 14) == [1, 0]
    assert get_human_age(14, 15) == [0, 1]


def test_should_return_one_for_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_for_more_than_15_and_less_than_24_ages() -> None:
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(20, 17) == [1, 1]


def test_should_return_two_for_first_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_correct_ages_for_more_than_24_25() -> None:
    assert get_human_age(24, 25) == [2, 2]
    assert get_human_age(26, 25) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
