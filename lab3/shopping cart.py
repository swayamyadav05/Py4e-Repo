# Defining a dictionary to store product info
product_info = {
    1: {"name": "Product 1", "price": 10.0, "quantity": 100},
    2: {"name": "Product 2", "price": 20.0, "quantity": 50},
    3: {"name": "Product 3", "price": 30.0, "quantity": 200}
}

# Defining a list to represent the shopping cart
cart = []

# Defining the functions to perform in shopping cart

# Add to cart
def add_to_cart(product_id, quantity):
    if product_id in product_info and product_info[product_id]["quantity"] >= quantity:
        cart.append({"id": product_id, "name": product_info[product_id]["name"], "price": product_info[product_id]["price"], "quantity": quantity})
        product_info[product_id]["quantity"] -= quantity
        print(f"{quantity} {product_info[product_id]['name']} added to cart.")
    else:
        print("Invalid product id or quantity")
        
# Viewing cart
def view_cart():
    print("Shopping Cart:")
    if len(cart) == 0:
        print("Cart is empty.")
    else:
        for item in cart:
            # print(f"{item['quantity']} {item['name']} - ${item['price']} each")
            print(f"{item['quantity']} {item['name']} - ${item['price']} each")
                
# Removing item from the cart
def remove_from_cart(product_id):
    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            product_info[product_id]["quantity"] += item["quantity"]
            print(f"{item['quantity']} {item['name']} removed form the cart.")
        else:
            print("Product not found.")

# Calculating total cost
def calcutale_total_cost():
    total_cost = 0.0
    for item in cart:
        total_cost += item["price"] * item["quantity"]
    print(f"Total cost: ${total_cost}")
    

add_to_cart(1, 20)
add_to_cart(2, 30)
add_to_cart(5, 29)
print()
view_cart()
print()
remove_from_cart(1)
print()
view_cart()
print()
add_to_cart(3, 30)
print()
view_cart()
print()
add_to_cart(3, 10)
print()
view_cart()
print()
calcutale_total_cost()