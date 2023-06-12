class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def get_all_products(self):
        return self.product_list

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def order(self, order_list):
        total_price = 0
        for product, quantity in order_list:
            if product not in self.product_list:
                raise Exception(f"Product {product.name} is not available in the store")
            if quantity > product.get_quantity():
                raise Exception(f"Insufficient quantity of {product.name} available")

            total_price += product.buy(quantity)

        return total_price
