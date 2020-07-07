# -*- coding: utf-8 -*-
import click

from models import Cart
from fixtures import (
    offers,
    chai,
    apple,
    coffee,
    milk,
    oatmeal,
    )


@click.command()
@click.option("--products", help="Share your products.")
def test_cart(products):
    print('Received products are {0}'.format(products))
    try:
        products = products.split(',')
        products = [eval(product) for product in products]
    except Exception as e:
        print('Unable to decode products, please try again')
    my_cart = Cart(products=products)
    Cart.calculate_total(my_cart, offers)

if __name__ == '__main__':
    test_cart()
