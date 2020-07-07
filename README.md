# Cart

- Maintain a cart of products and apply related offers/discounts to it.
- Need to ensure that there can be multiple discounts that can be applied to it

## Steps to run
1. ```git clone git@github.com:dhruvsingh/cart.git```
2. Make sure docker is installed, if not, run ```sudo apt install docker```
3. Next run docker build (with/without sudo as the case maybe) ```sudo -E docker build -t solution -f Dockerfile ..```
4. Next run docker run ```sudo -E docker run solution cart-calculator --products=apple,chai,milk```.
5. The available choices for products is : apple, chai, milk, oatmeal & coffee. These can be used in any combination.
6. Once step 4 is run, it'll print out products that were input and also the cart price/cost after applying discounts as mentioned. 


Scope
- No database is used, only used python classes, close to what a db ORM will offer

Extensibility
- Product class can be further extended to have category of the product for easier grouping
- Product can be a generic product, and be further drilled down to a Variant with a reference(FK) to product
- Offer can be split up into two classes further, one for storing the offer name, description and other Rule to store offer rules
