from conftest import *


class TestIngredient:
    @pytest.mark.parametrize(
        'fixture_name, expected_price',
        [
            ('sauce', 100),
            ('filling', 100)
        ]
    )
    def test_ingredient_get_price(self, request, fixture_name, expected_price): #Проверяем, что  возвращается правильная цена ингредиента.
        ingredient = request.getfixturevalue(fixture_name)
        assert ingredient.get_price() == expected_price

    @pytest.mark.parametrize(
        'fixture_name, expected_name',
        [
            ('sauce', "hot sauce"),
            ('filling', "cutlet")
        ]
    )
    def test_ingredient_get_name(self, request, fixture_name, expected_name): #Проверяем, что  возвращается правильное название ингредиента.
        ingredient = request.getfixturevalue(fixture_name)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize(
        'fixture_name, expected_type',
        [
            ('sauce', INGREDIENT_TYPE_SAUCE),
            ('filling', INGREDIENT_TYPE_FILLING)
        ]
    )
    def test_ingredient_get_type(self, request, fixture_name, expected_type): #Проверяем, что возвращается правильный тип ингредиента.
        ingredient = request.getfixturevalue(fixture_name)
        assert ingredient.get_type() == expected_type