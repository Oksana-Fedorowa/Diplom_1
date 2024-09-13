import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture()   #Создаем объект Bun с именем "black bun" и ценой 100.
def bun():
    bun = Bun("black bun", 100)
    return bun

@pytest.fixture()   #Создаем  mock объект класса Bun.
def mock_bun():
    mock_bun = Mock(Bun)
    mock_bun.get_name.return_value = "white bun"
    mock_bun.get_price.return_value = 200
    return mock_bun





@pytest.fixture()
def sauce():
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    return sauce

@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock(Ingredient)
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_sauce.get_name.return_value = "sour cream"
    mock_sauce.get_price.return_value = 200
    return mock_sauce

@pytest.fixture()# Создаем объект Ingredient с типом FILLING, названием "cutlet", и ценой 100.
def filling():
    filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    return filling

@pytest.fixture()
def mock_filling():
    mock_filling = Mock(Ingredient)
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_filling.get_name.return_value = "dinosaur"
    mock_filling.get_price.return_value = 200
    return mock_filling

@pytest.fixture()  #Создаем объект Burger, добавляем в него  булку и соус и начинку.
def full_burger(mock_bun, mock_sauce, mock_filling):
    full_burger = Burger()
    full_burger.set_buns(mock_bun)
    full_burger.add_ingredient(mock_sauce)
    full_burger.add_ingredient(mock_filling)
    return full_burger

@pytest.fixture()
def mock_ingredient():
    mock_ingredient = Mock(Ingredient)
    mock_ingredient.get_name.return_value = "hot sauce"
    mock_ingredient.get_price.return_value = 100
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient




