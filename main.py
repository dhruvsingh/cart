# -*- coding: utf-8 -*-
from models import Cart
from fixtures import products, offers


if __name__ == '__main__':
    # driver code for testing
    my_cart = Cart(products=products)
    Cart.calculate_total(my_cart, offers)
