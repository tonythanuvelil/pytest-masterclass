import pytest
from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock


@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_can_add_item(cart):
    cart.add("apple")
    assert cart.size() == 1


def test_is_item_added(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_cart_overflow(cart):
    for _ in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")


def test_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    """
    This mock_get_item and Mock ideally replaces the below price_map.
    This is used when mock database values are required to test a function.

    price_map = {
        "apple": 1.0,
        "orange": 2.0
    }
    """

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0
