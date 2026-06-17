import datetime
from write import save_products, Purchaseinvoicecreating, Saleinvoicecreating

"""
In this module four functions are created display_products, purchaseitem, new_product sellitem. In display_products, 
it displays the list of products in a tabular form. This function takes products as a parameter which is a list that contains
multiple products

purchaseitem allows the admin to restock one or more than one products stock. It asks the admin which product to restock by 
asking for product id and quantity unit. This function validates the input and updates the stock according to the inputted value
Then stores the value into the product.txt list and generates a purchaseitem invoice textfile
Parameters: It takes products as a parameters which is a list of productid, product name, brand ,cost price and country 

saleitem allows the admin to sell one or moer than one products. It asks admin about the customers name, phone and address then ask 
about the product id how many quantity to buy. This function validates the input and sell the stock according to the input value. 
Then updates the value into the product.txt list and generaes a sellitem invoice textfile
Parameters: It takes products as a parameters which is a list of productid, product name, brand ,cost price and country

newproduct allows the admin to add a new product into the list. It ask the admin to enter the product name, brand, quantity, price and
country. ID is printed by using +1 function and it gets adds into the exisitng products.txt file.
Parameters: It takes products as a parameters which is a list of productid, name ,brand,quantity, price and country.
"""

#function to display all the products 
def display_products(products):
    print("\nAvailable Products")
    print("-------------------------------------------------------------------------------")
    print("ID\tProduct Name\tBrand\t\tQty\tCostPrice\tCountry")
    print("-------------------------------------------------------------------------------")

    #looping through each products and printing the information in a tabular form
    for product in products:
        print(str(product[0]) + "\t" + product[1] + "\t" + product[2] + "\t" + str(product[3]) + "\t" +
              str(product[4]) + "\t\t" + product[5])
    print("-------------------------------------------------------------------------------")

#function to restock products
def purchaseitem(products):
    display_products(products)

    # Empty list to store restocked product and variable to store total price
    restocked_products = []
    total_price = 0

    while True:
        selected_products = []  # List to store product id
        quantities = []  # List to store restock quantity

        while True:
            # Asking for product ID
            while True:
                try:
                    productid = int(input("\nEnter the product ID you want to restock: "))
                    if productid <= 0 or productid > len(products):
                        print("Please choose a valid ID.")
                        continue
                    selected_products.append(productid) #adding the value into the selected_product list
                    break  # Exit the loop
                except ValueError:
                    print("Please enter a valid product ID.")
                    continue

            # Asking quantity to restock for selected product
            while True:
                try:
                    restock_quantity = int(input("Enter the quantity to restock: "))
                    if restock_quantity <= 0:
                        print("Please enter a valid quantity")
                        continue
                    quantities.append(restock_quantity)
                    break  # Exit the loop
                except ValueError:
                    print("Please enter a valid quantity.")
                    continue

            # Asking if the admin wants to restock multiple products
            while True:
                nextid = input("Do you want to restock another product? (yes/no): ").lower()
                if nextid == "no":
                    break
                elif nextid == "yes":
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
                    continue

            if nextid == "no":
                break  

        # Supplier name input validation
        while True:
            supplier_name = input("\nEnter the supplier's name: ")
            if supplier_name.replace(" ", "").isalpha():
                break
            else:
                print("Please enter a valid name.")

        # Looping through the selected product list and updating the stock
        for i in range(len(selected_products)):
            productid = selected_products[i]
            restock_quantity = quantities[i]
            selected_product = products[productid - 1]  # Getting the actual product data from the list

            # Updating the product stock with restock quantity
            selected_product[3] += restock_quantity

            # Calculating the cost for restocking a product
            price = restock_quantity * selected_product[4]
            total_price += price

            # Adding restocked product to the invoice list
            restocked_products.append({
                "product_name": selected_product[1],
                "restocked_quantity": restock_quantity,
                "new_stock": selected_product[3],
                "supplier": supplier_name,
                "cost": price,
                "brand": selected_product[2]
            })

            # Displaying the information
            print("\nProduct Restocked: " + selected_product[1] + " - " + str(restock_quantity) + " items added.")
            print("Supplier: " + supplier_name)
            print("Updated Stock: " + str(selected_product[3]))


        # Saving the product to the txt file
        save_products(products)

        # Showing updated product list
        print("\nUpdated product list:")
        display_products(products)

        # Generating a purchase invoice after restocking
        Purchaseinvoicecreating(restocked_products, total_price)

        # Asking if the admin wants to restock more products
        again = input("\nDo you want to restock more products? (yes/no): ").lower()
        if again != "yes":
            break


#function to sell products
def sellitem(products):
    print("-------------------------------------------------------------------------------")
    print("Please kindly input the customer's name, phone number and address")
    print("-------------------------------------------------------------------------------")

    #taking the customer name
    while True:
            name = str(input("Please enter the name: "))
            if name.isalpha():
                break
            else:
                print("Please enter a valid name.")

    #taking the phone number
    while True:
        try:
            phonenumber = int(input("Please enter the phone number: "))
            if phonenumber < 0:
                print("Please enter a positive 10 digit number .")
            elif len(str(phonenumber)) != 10:
                print("Phone number should be  10 digits.")
            else:
                break
        except ValueError:
            print("Please enter a valid phone number.")

    #taking the address
    while True:
            address = str(input("Please enter the address: "))
            if address.isalpha():
                break
            else: 
                print("Please enter a valid address")

    #displaying the product first to choose
    display_products(products)

    #empty selected_product, invoice_items to store product id and invoice items
    selected_products = []
    invoice_items = []
    total_price = 0 #storing the total price of the sold values

    while True:
        try:
            productid = int(input("Enter a product ID to sell: "))
            if productid <= 0 or productid > len(products):
                print("Please enter a valid product ID.")
                continue
            selected_products.append(productid)
        except ValueError:
            print("Please enter a valid product ID.")
            continue

        while True:
            nextid = input("Do you want to sell another product? (yes/no): ").lower()
            if nextid == "yes":
                break
            elif nextid == "no":
                break
            else:
                print("Please enter 'yes' or 'no'.")
                continue
        if nextid == "no":
                break

    #entering quantity for selected products
    for productid in selected_products:
        selected_product = products[productid - 1]
        selected_quantity = selected_product[3]

        while True:
            try:
                productquantity = int(input("Enter quantity to sell for " + selected_product[1] + " (Available: " + str(selected_quantity) + "): "))
                if productquantity <= 0:
                    print("Please enter a valid quantity amount")
                    continue
                if productquantity > selected_quantity:
                    print("Oops! Looks like the stock has run out. Please choose a different quantity.")
                    continue
                break 
            except ValueError:
                print("Please enter a valid quantity amount.")

        #calculating the buy three get one free policy
        max_free = productquantity // 3
        remaining_stock_after_purchase = selected_quantity - productquantity

        #check if free items doesnt exceeds the amount of stock
        if max_free > remaining_stock_after_purchase:
            freeitems = remaining_stock_after_purchase
            stock_limited = True
        else:
            freeitems = max_free
            stock_limited = False

        #to get the total quantity of selected product and free items
        totalquantity = productquantity + freeitems
        price = productquantity * selected_product[4]
        total_price += price

        #appending to the invoice_item to generate invoice 
        invoice_items.append({
            'type': selected_product[1],
            'brand': selected_product[2],
            'quantity': productquantity,
            'free_items': freeitems,
            'price': price
        })

        #updating stock by reducing the quantity bough
        selected_product[3] -= totalquantity

        #checking if full free item recieved or not
        if freeitems > 0:
            if stock_limited:
                print("\nDue to limited stock, you received only " + str(freeitems) + " free item(s) instead of " + str(max_free) + ".")
                print("\n")

            else:
                print("\nCongrats on getting " + str(freeitems) + " free item(s) as part of our 'Buy Three Get One Free' policy.")
                print("\n")

        else:
            print("\nBuy three items and get one free. Don't miss our 'Buy Three Get One Free' offer!")
            print("\n")


    #generating invoice passing different parameters
    Saleinvoicecreating(name, phonenumber, address, invoice_items, total_price)

    print("\nThank you! Purchase successful.")
    for item in invoice_items:
        print(str(item['quantity']) + " + " + str(item['free_items']) + " free of " + item['type'] + " (" + item['brand'] + ")")

    #saving updated value to the file 
    save_products(products)

    print("\nUpdated product list:")
    display_products(products)

def new_product(products):
    while True:
        #taking product name
        product_name = input("Please enter the product name: ")
        if product_name.isalpha():  # Ensure name is alphabetic
            break
        else:
            print("Please enter a valid name.")

    while True:
        #taking product brand name
        brand = input("Enter product brand: ")
        if brand.isalpha():
            break
        else:
            print("Please enter a valid brand name.")

    while True:
        #taking product price
        try:
            price = float(input("Enter price of the product: "))
            if price <= 0:
                print("Please enter a valid price.")
                continue
            break
        except ValueError:
            print("Please enter a valid price.")
    
    while True:
        #taking product quantity
        try:
            quantity = int(input("Enter quantity for the product: "))
            if quantity <= 0:
                print("Please enter a valid quantity.")
                continue
            break
        except ValueError:
            print("Please enter a valid quantity.")

    while True:
        #taking country of origin for the product
        country = input("Enter country of origin: ")
        if country.isalpha(): 
            break
        else:
            print("Please enter a valid country name.")

    #creating add product adding the new product to the product list
    add_product = [len(products) + 1, product_name, brand, quantity, price, country]
    products.append(add_product)

    print("\nNew product added: " + str(add_product))

    save_products(products)

    print("\nUpdated product list:")
    display_products(products)

    #add another product to the list
    while True:
        nextid = input("Do you want to add another product? (yes/no): ").lower()
        if nextid == "yes":
            return new_product(products)#calling the function again due to no loop
        elif nextid == "no":
            break 
        else:
            print("Please enter 'yes' or 'no'.")
            continue
