import pytest
from praktikum.database import Database


class TestDatabase:
    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ]
    )
    def test_available_buns(self, index, expected_name, expected_price):
        db = Database()
        buns = db.available_buns()
        assert (len(buns) == 3 and buns[index].get_name() == expected_name and
                buns[index].get_price() == expected_price)

    @pytest.mark.parametrize("index, expected_type, expected_name, expected_price", [
        (0, 'SAUCE', "hot sauce", 100),
        (1, 'SAUCE', "sour cream", 200),
        (2, 'SAUCE', "chili sauce", 300),
        (3, 'FILLING', "cutlet", 100),
        (4, 'FILLING', "dinosaur", 200),
        (5, 'FILLING', "sausage", 300),
    ])
    def test_available_ingredients(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ingredients = db.available_ingredients()

        assert (len(ingredients) == 6 and
                ingredients[index].get_type() == expected_type and
                ingredients[index].get_name() == expected_name and
                ingredients[index].get_price() == expected_price)
