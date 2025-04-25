from functions import *

def menu():
	while True:
		print("\nMenu:")
		print("1. Add Products")
		print("2. Remove Products")
		print("3. Show Product List")
		print("4. Calculate Total Cost")
		print("5. Insert Discount Coupon")
		print("6. Exit")

		choice = input("Enter your choice: ").strip()

		if choice == "6":
				print("Exiting the program...")
				break

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
		else:
				print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
