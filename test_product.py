import pytest
from products import Product


def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_invalid_product():
    with pytest.raises(ValueError):
        product = Product("", price=-500, quantity=50)  # Empty name and negative price


def test_product_becomes_inactive():
    product = Product("Headphones", price=50, quantity=1)
    assert product.is_active() is True
    product.buy(1)
    assert product.is_active() is False


def test_product_purchase():
    product = Product("Phone", price=300, quantity=10)
    assert product.get_quantity() == 10
    total_price = product.buy(3)
    assert product.get_quantity() == 7
    assert total_price == 900


def test_buying_larger_quantity():
    product = Product("Tablet", price=200, quantity=5)
    with pytest.raises(Exception):
        total_price = product.buy(10)
