# -*- coding: utf-8 -*-
def apply_discounts(product_status, cart):

    for product, product_offer in product_status.items():
        product_offers = product_offer['offers']
        prices_list = []

        for offer in product_offers:
            cart_total = cart.total
            if (
                    offer.dependent.name in product_status
                    and offer.product.name in product_status
                    and offer.product.name == product
            ):
                while (
                    product_status[offer.product.name]['quantity'] >= offer.order_quantity
                    and product_status[offer.dependent.name]['quantity'] > 0
                    and (not offer.limit or offer.limit > 0)
                ):
                    if offer.condition != '>=':
                        product_status[offer.dependent.name]['quantity'] -= 1

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
    """If any of the product or dependent is current product, then offer is available"""
    applicable_offers = set()

    for offer in offers:
        if offer.product == product or offer.dependent == product:
            applicable_offers.add(offer)

    return applicable_offers


def get_offers(cart, offers):
    """
    Build a key, value
    """
    product_status = {}

    for product in cart.products:
        product_offers = get_offers_for_product(product, offers)

        try:
            product_status[product.name]['quantity'] += 1
            product_status[product.name]['offers'].update(product_offers)
        except KeyError:
            product_status[product.name] = {
                'quantity': 1, 'offers': product_offers,
                'product': product
            }

    return product_status


class Base(object):
    """Abstract class to have id/timestamp fields as standard."""

    class Meta:
        abstract = True


class Product(Base):
    """
    Holds information about a unique product; price and name for now.

    Can be extended using Variant class to hold multiple variants for a product.
    """

    def __init__(self, code: str, name: str, price: float, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
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
        super(self.__class__, self).__init__()
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'{self.name}'

    __str__ = __repr__


class Cart(Base):
    """
    Holds information about products; price and name for now.
    """

    def __init__(self, products: [Product], *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.products = products
        self.total = 0.0

    def add_product(self, product: Product):
        # add product to the cart and calculate current cart status?
        self.products.append(product)

    def remove_product(self, product: Product):
        # needed later?
        pass

    @staticmethod
    def calculate_total(cart, offers):
        """
        Calculate cart total.

        Apply discounts too.
        """
        for product in cart.products:
            cart.total += product.price

        product_status = get_offers(cart, offers)
        apply_discounts(product_status, cart)

        print(
            '{products} are in cart.'.format(
                products=', '.join([product.name for product in cart.products])
            )
        )
        print('Cart total is ${total}'.format(total=round(cart.total, 2)))
