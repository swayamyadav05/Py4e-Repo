# Define a dictionary to store product information
products = {
    1: {"name": "Product 1", "price": 10.0, "quantity": 100},
    2: {"name": "Product 2", "price": 20.0, "quantity": 200},
    3: {"name": "Product 3", "price": 30.0, "quantity": 300}
}

# Define a list to represent the shopping cart
cart = []

# Define functions to perform operations on the shopping cart

def add_to_cart(product_id, quantity):
    if product_id in products and products[product_id]["quantity"] >= quantity:
        cart.append({"id": product_id, "name": products[product_id]['name'], "price": products[product_id]['price'], "quantity": quantity})
        products[product_id]['quantity'] -= quantity
        print(f"{quantity} {products[product_id]['name']} added to the cart")
    else:
        print("Product not found or not enough.")

def view_cart():
    print("Shopping Cart:")
    if len(cart) == 0:
        print("Cart is empty.")
    else:
        for item in cart:
            print(f"{item['quantity']} {item['name']} - ${item['price']} each")
                  
def remove_from_cart(product_id):
    for item in cart:
        if item['id'] == product_id:
            cart.remove(item)
            products[product_id]['quantity'] += item['quantity']
            print(f"{item['quantity']} {item['name']} removed fromt the cart")
        else:
            print("Product not found.")

def calculate_total_cost():
    total_cost = 0.0
    for item in cart:
        total_cost += item['price'] * item['quantity']
    print(f"Total cost: ${total_cost}")
    
add_to_cart(1, 30)
print()
view_cart()
print()
add_to_cart(2, 50)
print()
view_cart()
print()
remove_from_cart(2)
print()
view_cart()
print()
calculate_total_cost()