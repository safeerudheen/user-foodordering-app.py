class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []  # List to store user's orders

class FoodItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

users = []  # List to store user objects
food_items = [FoodItem("Tandoori Chicken (4 pieces)", "4 pieces", 240),
              FoodItem("Vegan Burger (1 Piece)", "1 piece", 320),
              FoodItem("Truffle Cake (500gm)", "500gm", 900)]

def register_user():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    user = User(full_name, phone_number, email, address, password)
    users.append(user)
    print("User registered successfully!")

def user_login():
    username = input("Enter your email: ")
    password = input("Enter your password: ")
    for user in users:
        if user.email == username and user.password == password:
            print("User login successful!")
            return user  # Return the logged-in user object
    print("Invalid email or password. User login failed.")
    return None  # Return None to indicate login failure

def place_new_order(user):
    print("\nPlace New Order")
    if not food_items:
        print("No food items available for ordering.")
        return

    print("\nAvailable Food Items:")
    for i, food_item in enumerate(food_items, start=1):
        print(f"{i}. {food_item.name} [{food_item.quantity}] [INR {food_item.price}]")

    selected_items = input("Enter the numbers of the items you want to order (e.g., 1 2): ").split()
    order = []

    for item in selected_items:
        try:
            index = int(item) - 1
            if 0 <= index < len(food_items):
                order.append(food_items[index])
            else:
                print(f"Invalid item number: {item}")
        except ValueError:
            print(f"Invalid input: {item}")

    if not order:
        print("No items selected for the order.")
        return

    print("\nItems selected for the order:")
    total_price = 0
    for i, item in enumerate(order, start=1):
        print(f"{i}. {item.name} [{item.quantity}] [INR {item.price}]")
        total_price += item.price

    print(f"Total Price: INR {total_price}")

    confirm = input("Do you want to place the order (yes/no)? ").strip().lower()
    if confirm == 'yes':
        user.orders.append(order)
        print("Order placed successfully!")
    else:
        print("Order not placed.")

def order_history(user):
    print("\nOrder History")
    if not user.orders:
        print("You haven't placed any orders yet.")
    else:
        for i, order in enumerate(user.orders, start=1):
            print(f"Order {i}:")
            total_price = 0
            for item in order:
                print(f"{item.name} [{item.quantity}] [INR {item.price}]")
                total_price += item.price
            print(f"Total Price: INR {total_price}")

def update_user_profile(user):
    print("\nUpdate User Profile")
    print(f"Full Name: {user.full_name}")
    print(f"Phone Number: {user.phone_number}")
    print(f"Email: {user.email}")
    print(f"Address: {user.address}")

    choice = input("Do you want to update your profile (yes/no)? ").strip().lower()
    if choice == 'yes':
        full_name = input(f"Enter new full name ({user.full_name}): ") or user.full_name
        phone_number = input(f"Enter new phone number ({user.phone_number}): ") or user.phone_number
        address = input(f"Enter new address ({user.address}): ") or user.address

        user.full_name = full_name
        user.phone_number = phone_number
        user.address = address
        print("User profile updated successfully.")

logged_in_user = None  # Initialize the logged-in user as None

while True:
    print("\nFood Ordering App")
    if logged_in_user is None:
        print("1. Register User")
        print("2. User Login")
    else:
        print(f"Logged in as {logged_in_user.full_name}")
        print("3. Place New Order")
        print("4. Order History")
        print("5. Update Profile")
        print("6. Logout")

    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_user()
    elif choice == '2':
        if logged_in_user is None:
            logged_in_user = user_login()
        else:
            print("User is already logged in.")
    elif choice == '3':
        if logged_in_user is not None:
            place_new_order(logged_in_user)
        else:
            print("You need to log in as a user first.")
    elif choice == '4':
        if logged_in_user is not None:
            order_history(logged_in_user)
        else:
            print("You need to log in as a user first.")
    elif choice == '5':
        if logged_in_user is not None:
            update_user_profile(logged_in_user)
        else:
            print("You need to log in as a user first.")
    elif choice == '6':
        logged_in_user = None
        print("Logged out.")
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")