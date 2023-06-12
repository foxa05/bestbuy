from products import Product, LimitedProduct, NonStockedProduct


class Promotion:
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, price, quantity):
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, price, quantity):
        return (price * quantity) / 2


class ThirdOneFree(Promotion):
    def apply_promotion(self, price, quantity):
        return price * (quantity - (quantity // 3))


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, price, quantity):
        discount = price * self.percent / 100
        return price * quantity - discount


class Store:
    def __init__(self, products):
        self.products = products

    def get_all_products(self):
        return self.products

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def order(self, order_list):
        total_price = 0
        for product, quantity in order_list:
            if product not in self.products:
                raise Exception(f"Product {product.name} is not available in the store")
            if quantity > product.get_quantity():
                raise Exception(f"Insufficient quantity of {product.name} available")

            total_price += product.buy(quantity)

        return total_price

def view_all_products(store):
    print("---- All Products ----")
    products = store.get_all_products()
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.show()}")

# Rest of the code...



product_list = [
    LimitedProduct("MacBook Air M2", price=1450, quantity=100, maximum=2),
    LimitedProduct("Bose QuietComfort Earbuds", price=250, quantity=500, maximum=3),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion objects
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)


# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = Store(product_list)
