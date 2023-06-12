from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def show(self):
        promotion_info = self.promotion.name if self.promotion else "None"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {promotion_info}"

    def buy(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            if self.promotion:
                return self.promotion.apply_promotion(self) * quantity
            else:
                return self.price * quantity
        else:
            raise Exception("Insufficient quantity available for purchase")



class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        promotion_info = self.promotion.name if self.promotion else "None"
        quantity_info = f"Quantity: {self.quantity}, Limited to {self.maximum} per order!"
        return f"{self.name}, Price: ${self.price}, {quantity_info}, Promotion: {promotion_info}"

    def buy(self, quantity):
        if quantity <= self.quantity and quantity <= self.maximum:
            self.quantity -= quantity
            if self.promotion:
                return self.promotion.apply_promotion(self) * quantity
            else:
                return self.price * quantity
        else:
            raise Exception("Invalid quantity or exceeds maximum limit")


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product):
        return product.price / 2


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product):
        quantity_to_pay = product.quantity - (product.quantity // 3)
        return product.price * quantity_to_pay


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product):
        discount = (self.percent / 100) * product.price
        return product.price - discount


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        raise Exception("Cannot set quantity for a non-stocked product")

    def buy(self, quantity):
        raise Exception("Cannot purchase a non-stocked product")
