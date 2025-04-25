import re

products = []
discount_coupon = 0

def get_valid_name(prompt):
	pattern = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s]+$'
	while True:
		value = input(prompt).strip()
		if re.match(pattern, value):
			return value
		print("Please enter a valid product name (letters, numbers, and spaces only).")

def get_positive_int(prompt):
	while True:
		value = input(prompt)
		if value.isdigit() and int(value) > 0:
			return int(value)
		print("Please enter a positive integer (no decimals, letters, or special characters).")

def get_non_negative_percentage(prompt):
	while True:
		try:
			value = float(input(prompt))
			if 0 <= value <= 100:
					return value
			else:
					print("The percentage must be a number between 0 and 100.")
		except ValueError:
				print("Invalid percentage, please enter a valid number.")

def add_product():
	name = get_valid_name("Enter product name: ")
	price = get_positive_int("Enter the unit price of the product (integer only): ")
	quantity = get_positive_int("Enter the quantity (integer only): ")

	product = {
			"name": name,
			"price": price,
			"quantity": quantity
	}

	products.append(product)
	print("The product was added successfully.")

def remove_product():
	if not products:
		print("No products to remove.")
		return

	show_products()
	try:
		index = int(input("Enter the product number to remove: ")) - 1
		if 0 <= index < len(products):
			removed = products.pop(index)
			print(f"Removed product: {removed['name']}")
		else:
			print("Invalid product number.")
	except ValueError:
			print("Please enter a valid number.")

def show_products():
	if not products:
		print("No products added yet.")
		return

	print("\n--- Product List ---")
	total = 0
	for i, product in enumerate(products, 1):
		unit_price = product["price"]
		quantity = product["quantity"]
		total_price = unit_price * quantity
		total += total_price
		print(f"{i}. {product['name']}")
		print(f"   - Unit Price: ${unit_price:.2f}")
		print(f"   - Quantity: {quantity}")
		print(f"   - Total: ${total_price:.2f}")
	print(f"\nSubtotal of all products: ${total:.2f}")

def calculate_total_cost():
	if not products:
			print("No products to calculate.")
			return

	subtotal = sum(p["price"] * p["quantity"] for p in products)
	discount_amount = subtotal * (discount_coupon / 100)
	total = subtotal - discount_amount

	print("\n--- Purchase Summary ---")
	print(f"Subtotal: ${subtotal:.2f}")
	print(f"Discount Coupon: {discount_coupon:.2f}% (-${discount_amount:.2f})")
	print(f"Total Cost: ${total:.2f}")

def insert_discount_coupon():
	global discount_coupon
	if not products:
			print("You need to add at least one product before applying a discount coupon.")
			return

	discount_coupon = get_non_negative_percentage("Enter discount percentage coupon (0-100): ")
	print(f"Coupon of {discount_coupon}% applied to total.")

def menu():
	while True:
		print("\nMenu:")
		print("1. Add Products")
		print("2. Remove Products")
		print("3. Show Product List")
		print("4. Calculate Total Cost")
		print("5. Insert Discount Coupon")
		print("6. Exit")

		choice = input("Enter your choice: ")

		if choice == "1":
				add_product()
		elif choice == "2":
				remove_product()
		elif choice == "3":
				show_products()
		elif choice == "4":
				calculate_total_cost()
		elif choice == "5":
				insert_discount_coupon()
		elif choice == "6":
				print("Exiting the program...")
				break
		else:
				print("Invalid choice. Please try again.")

menu()
