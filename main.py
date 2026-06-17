from read import read_products
from operations import purchaseitem, sellitem, display_products, new_product

"""
Main function that runs the WeCare Store System. 

The main() provides the admin with a CLI interface to manage the WeCare Store management system that allows the admin
to use different menu function like. Display all products, Sell products, Restocking products (buying from a supplier) and 
exiting the program. Importing different functions like read_products, display_products, purchases item and sellitem from 
read and operation module 

This function takes no parameters 
"""
def main():
    file_path = 'products.txt' #file path 

    while True:
        #reads the products and gives list into product_list in a loop
        product_list = read_products(file_path)

        #Displays WeCare Store info and header
        print("\n\n")
        print("\t \t \t \t \t \t \tWe Care Store")
        print("\n")
        print("\t \t \t \t \tChaunni, Kathmandu || Phone No: 9861230823")
        print("\t \t \t \t \t \t \tThen | Now | Forever")
        print("\n")
        print("\n----------------")
        print("\nWelcome to the WeCare Store System Admin!")
        print("Admin Menu")
        print("------------------")
        print("1. Display Products")
        print("2. Sell Products")
        print("3. Restock Products")
        print("4. Add new products")
        print("5. Exit")

        #gives admin options to choose between 1 to 5
        option = input("\nEnter an option (1-5): ")

        if option == '1':
            display_products(product_list)
        elif option == '2':
            sellitem(product_list)
        elif option == '3':
            purchaseitem(product_list)
        elif option == '4':
            new_product(product_list)
        elif option == '5':
            print("\nThank you for using the WeCare Skin Care Product Sale System. Goodbye!")
            break
        else:
            print("Please choose a valid option")

        #pausing in between different menus
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
