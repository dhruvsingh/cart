# Cart

- Maintain a cart of products and apply related offers/discounts to it.
- Need to ensure that there can be multiple discounts that can be applied to it

## Steps to run
1. ```git clone git@github.com:dhruvsingh/cart.git```
2. Make sure docker and docker-compose are installed, if not, run ```sudo apt install docker docker-compose```
3. ```docker-compose up```
4. The above line will print the products and the cart total, after applying discounts if any.


Scope
- No database is used, only used python classes, close to what a db ORM will offer

Extensibility
- Product class can be further extended to have category of the product for easier grouping
- Product can be a generic product, and be further drilled down to a Variant with a reference(FK) to product
- Offer can be split up into two classes further, one for storing the offer name, description and other Rule to store offer rules
