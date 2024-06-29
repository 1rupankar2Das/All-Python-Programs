# Build classes for products, customers, and a shopping cart. Implement 
# methods for adding/removing items, calculating total cost, and 
# processing orders.
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price})"

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.shopping_cart = ShoppingCart(self)

    def __str__(self):
        return f"Customer(id={self.customer_id}, name={self.name})"

class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}

    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        print(f"Added {quantity} of {product.name} to the cart.")

    def remove_item(self, product, quantity):
        if product.product_id in self.items:
            if self.items[product.product_id]['quantity'] <= quantity:
                removed_quantity = self.items[product.product_id]['quantity']
                del self.items[product.product_id]
                print(f"Removed {removed_quantity} of {product.name} from the cart.")
            else:
                self.items[product.product_id]['quantity'] -= quantity
                print(f"Removed {quantity} of {product.name} from the cart.")
        else:
            print(f"Product {product.name} is not in the cart.")

    def calculate_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        print(f"Total cost is ${total:.2f}.")
        return total

    def process_order(self):
        if not self.items:
            print("Cart is empty. Cannot process order.")
            return 0
        total_cost = self.calculate_total()
        self.items.clear()  # Empty the cart after processing the order
        print(f"Order processed for {self.customer.name}. Total cost: ${total_cost:.2f}.")
        return total_cost

    def __str__(self):
        item_list = [f"{item['product'].name} (x{item['quantity']})" for item in self.items.values()]
        return f"ShoppingCart(items={', '.join(item_list)})"

# Example usage
product1 = Product("P001", "Laptop", 999.99)
product2 = Product("P002", "Smartphone", 599.99)
product3 = Product("P003", "Headphones", 199.99)

customer1 = Customer("C001", "Alice")

# Adding products to the shopping cart
customer1.shopping_cart.add_item(product1, 1)
customer1.shopping_cart.add_item(product2, 2)
customer1.shopping_cart.add_item(product3, 3)

# Removing a product from the shopping cart
customer1.shopping_cart.remove_item(product2, 1)

# Calculating the total cost of the shopping cart
customer1.shopping_cart.calculate_total()

# Processing the order
customer1.shopping_cart.process_order()
