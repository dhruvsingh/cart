# -*- coding: utf-8 -*-
from decimal import Decimal

from models import Product, Offer

chai = Product(code='CH1', name='Chai', price=Decimal(3.11))
apple = Product(code='AP1', name='Apple', price=Decimal(6.00))
coffee = Product(code='CF1', name='Coffee', price=Decimal(11.23))
milk = Product(code='MK1', name='Milk', price=Decimal(4.75))
oatmeal = Product(code='OM1', name='Oatmeal', price=Decimal(3.69))


offers = [
    Offer(**{
        'name': 'BOGO',
        'product': coffee,
        'order_quantity': 2,
        'factor': 1,
        'type': 'P',
        'dependent': coffee,
        'condition': '=',
        'offer': Decimal(0.5),
        'limit': None
    }),
    Offer(**{
        'name': 'APPL',
        'product': apple,
        'order_quantity': 3,
        'factor': 3,
        'type': 'P',
        'dependent': apple,
        'condition': '>=',
        'offer': Decimal(0.25),
        'limit': None
    }),
    Offer(**{
        'name': 'CHMK',
        'product': chai,
        'order_quantity': 1,
        'factor': 1,
        'type': 'P',
        'dependent': milk,
        'condition': '=',
        'offer': 1,
        'limit': 1,
    }),
    Offer(**{
        'name': 'APOM',
        'product': oatmeal,
        'order_quantity': 1,
        'factor': 1,
        'type': 'P',
        'dependent': apple,
        'condition': '=',
        'offer': Decimal(0.5),
        'limit': 1,
    })
]
