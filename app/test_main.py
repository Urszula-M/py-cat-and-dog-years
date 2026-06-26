import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="zero_ages"),
        pytest.param(14, 14, [0, 0], id="both_under_15"),
        pytest.param(15, 14, [1, 0], id="cat_15_dog_14"),
        pytest.param(14, 15, [0, 1], id="cat_14_dog_15"),
        pytest.param(15, 15, [1, 1], id="both_exactly_15_years"),
        pytest.param(16, 16, [1, 1], id="both_between_15_and_24"),
        pytest.param(23, 23, [1, 1], id="both_almost_24"),
        pytest.param(20, 17, [1, 1], id="mixed_ages_between_15_and_24"),
        pytest.param(24, 24, [2, 2], id="both_exactly_24_years"),
        pytest.param(24, 25, [2, 2], id="cat_24_dog_25"),
        pytest.param(26, 25, [2, 2], id="cat_26_dog_25"),
        pytest.param(28, 28, [3, 2], id="cat_28_dog_28"),
        pytest.param(100, 100, [21, 17], id="both_100_years")
    ]
)
def test_should_convert_animals_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
