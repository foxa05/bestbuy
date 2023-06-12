from products import Product
from store import Store

def display_menu():
    print("--------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def view_all_products(store):
    print("---- All Products ----")
    products = store.get_all_products()
    for product in products:
        product.show()

def view_total_quantity(store):
    total_quantity = store.get_total_quantity()
    print("---- Total Quantity ----")
    print(f"Total Quantity: {total_quantity}")

def order_products(store):
    print("---- Order Products ----")
    products = store.get_all_products()
    order_list = []
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.name}")
    print("0. Exit")

    while True:
        print("When you want to finish order, enter empty text.")
        choice = input("Which product # do you want? ")
        if choice == '0' or choice == '':
            break
        try:
            product_index = int(choice) - 1
            if product_index < 0 or product_index >= len(products):
                raise ValueError
            quantity = int(input("What amount do you want? "))
            order_list.append((products[product_index], quantity))
            print("Product added to order")
        except ValueError:
            print("Invalid input. Please try again.")

    if order_list:
        try:
            total_price = store.order(order_list)
            print(f"Order placed successfully. Total price: {total_price}")
        except Exception as e:
            print(f"Failed to place order: {str(e)}")
    else:
        print("No products were ordered")

def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            view_all_products(best_buy)
        elif choice == '2':
            view_total_quantity(best_buy)
        elif choice == '3':
            order_products(best_buy)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        print()

if __name__ == '__main__':
    main()
