from conftest import *


class TestBurger:
    def test_initial_state(self, burger): #проверяется начальное состояние объекта Burger
        assert burger.bun is None and len(burger.ingredients) == 0

    def test_set_bun(self, burger, mock_bun): #Проверяет установку булки в бургер.
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_sauce): #Проверяет добавление ингредиента в бургер
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_burger_move_ingredient(self, full_burger, mock_sauce):
        full_burger.move_ingredient(0, 1)
        assert full_burger.ingredients[1] == mock_sauce  #Проверяет перемещение ингредиента в бургере


    def test_get_price(self, full_burger): #проверяет правильность расчета цены
        assert full_burger.get_price() == 800

    def test_burger_get_receipt(self, full_burger):
        assert full_burger.get_receipt() == ('(==== white bun ====)\n'
                                             '= sauce sour cream =\n'
                                             '= filling dinosaur =\n'
                                             '(==== white bun ====)\n'
                                             '\n'
                                             'Price: 800')