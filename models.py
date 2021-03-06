# -*- coding: utf-8 -*-
from typing import List
from decimal import Decimal


def apply_discounts(product_status, cart):
    """Apply discounts on cart per the products that it contains."""

    for product, product_offer in product_status.items():
        product_offers = product_offer['offers']
        prices_list = []

        for offer in product_offers:
            cart_total = cart.total
            offer_limit = offer.limit or True
            if (
                    offer.dependent.name in product_status
                    and offer.product.name in product_status
                    and offer.product.name == product
            ):
                while (
                    product_status[offer.product.name]['quantity'] >= offer.order_quantity
                    and product_status[offer.dependent.name]['quantity'] > 0
                    and offer_limit > 0
                ):
                    if offer.condition != '>=':
                        product_status[offer.dependent.name]['quantity'] -= 1

                    if isinstance(offer_limit, int):
                        offer_limit -= 1

                    product_status[offer.product.name]['quantity'] -= offer.order_quantity

                    cart_total -= (
                            offer.offer
                            * offer.dependent.price
                            * offer.order_quantity
                    )
                prices_list.append(cart_total)

        if prices_list:
            cart.total = min(prices_list)


def get_offers_for_product(product, offers):
    """Accumulate all offers applicable for a product."""
    applicable_offers = set()

    for offer in offers:
        if offer.product == product or offer.dependent == product:
            applicable_offers.add(offer)

    return applicable_offers


def get_offers(cart, offers):
    """
    Build a key, value store with product quantity, and applicable offers.
    """
    product_status = {}

    for product in cart.products:
        product_offers = get_offers_for_product(product, offers)

        try:
            product_status[product.name]['quantity'] += 1
            product_status[product.name]['offers'].update(product_offers)
        except KeyError:
            product_status[product.name] = {
                'quantity': 1,
                'offers': product_offers,
            }

    return product_status


class Base(object):
    """Abstract class to have id/timestamp fields as standard."""

    class Meta:
        abstract = True


class Product(Base):
    """
    Holds information about a unique product; code, price and name for now.

    Can be extended using Variant class to have multiple variants for a product.
    """

    def __init__(self, code: str, name: str, price: float, *args, **kwargs):
        self.code = code
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.code} - {self.name}'

    __str__ = __repr__


class Offer(Base):
    """
    Holds information about available coupons and application per product.
    """

    def __init__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)

    def __repr__(self):
        return f'{self.name}'

    __str__ = __repr__


class Cart(Base):
    """
    Holds information about products; price and name for now.
    """

    def __init__(self, products: List[Product], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = products
        self.total = Decimal(0.0)

    def add_product(self, product: Product):
        # add product to the cart and calculate current cart status?
        self.products.append(product)

    def remove_product(self, product: Product):
        # needed later?
        pass

    @staticmethod
    def calculate_total(cart, offers):
        """
        Calculate cart total with available offers.
        """
        for product in cart.products:
            cart.total += product.price

        product_status = get_offers(cart, offers)
        apply_discounts(product_status, cart)

        print(
            f"{', '.join([product.name for product in cart.products])} are in cart."
        )
        print(f'Cart total is ${round(cart.total, 2)}')
