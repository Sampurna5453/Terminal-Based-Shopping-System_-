import datetime
"""
This module contains save_products, Purchaseinvoicecreating and Saleinvoicecreating
save_products function takes all the product in list format as parameters used to overwrite exisitng data in the txtfile.

Purchaseinvoicecreating generates a restock invoice text file for restocking products that contains details about restocked
product, supplier name, restocked quantity and total amount
Parameters: Only takes total_price (Total cost of restocked products) and restocked_products(list of dictaionaries containing 
productname, restocked quantity, new_stock nd supplier name)

Saleinvoice creating generates a sale invoice file for sold products in a txt file that includes customer name, phone, address
item purchased, quantity sold, free items and a unique invoice ID for each invoice file.
Parameters: name (Customer name), phonenumber(Num of customer), address(Customer address), invoice_items (list of dictionaries 
that contains type, brand, quantity, free items and price), total_price(Total transaction amount)
"""
def save_products(products):
    with open("products.txt", "w") as file:
        for product in products: #loop through each product
            name = product[1]
            brand = product[2]
            quantity = product[3]
            selling_price = product[4]
            country = product[5]

            #calculating cost price by reversing 200% increase 
            cost_price = selling_price / 3

            #variable name line that writes data in list format
            line = name + "," + brand + "," + str(quantity) + "," + str(cost_price) + "," + country + "\n"
            file.write(line)


#function to create restocking product
def Purchaseinvoicecreating(restocked_products, total_price):
    import datetime
    now = datetime.datetime.now()

    #unique value using hour, minute and second 
    timing = str(now.hour) + str(now.minute) + str(now.second)

    #assiniging invoice file name
    if restocked_products:
        product_name = restocked_products[0]['product_name']
    else:
        product_name = "UnknownProduct"

    #filename using productname and uniquevalue created.
    fileName = "PurchaseInvoice_" + product_name + "_" + timing + ".txt"

    with open(fileName, "w") as file:
        file.write("===========================================\n")
        file.write("\tWeCare Store Invoice\n")
        file.write("===========================================\n")
        file.write("\n")
        file.write("\t  Purchase Invoice\n")
        file.write("-------------------------------------------\n")
        invoice_id = "WeCare " + timing
        file.write("Invoice ID: " + invoice_id + "\n")
        file.write("Customer Name: WeCare Store \n")
        file.write("Phone Number: 9861230823\n")
        file.write("Address: Chaunni\n")
        #writing current year month day hour minute and second
        date_time = ("Date: " + str(now.year) + "-" + str(now.month) + "-" + str(now.day) +
            " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        )
        file.write(date_time + "\n")
        file.write("-------------------------------------------\n")

        #looping through each restocked product and printing the details
        for item in restocked_products:
            file.write("Product Name: " + item['product_name'] + "\n")
            file.write("Brand Name: " + item['brand'] + "\n")
            file.write("Quantity Restocked: " + str(item['restocked_quantity']) + "\n")
            file.write("Updated Stock: " + str(item['new_stock']) + "\n")
            file.write("Supplier name: " + item['supplier'] + "\n")
            file.write("-------------------------------------------\n")

        #adding the total 
        file.write("TOTAL AMOUNT: Rs. " + str(total_price) + "\n")
        file.write("===========================================\n")
        file.write("Thank you for shopping with us. Hope you have a great day!\n")
        file.write("\nWe Care Store")

    #message to inform an invoice has been created 
    print("\nPurchase invoice generated successfully: " + fileName)

def Saleinvoicecreating(name, phonenumber, address, invoice_items, total_price):
    now = datetime.datetime.now()
    timing = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
    #creating a new invoice file
    filename = "Saleinvoice_" + name + "_" + timing + ".txt"
    with open(filename, "w") as file:
            file.write("===========================================\n")
            file.write("\tWeCare Store Invoice\n")
            file.write("===========================================\n")
            file.write("\n")
            file.write("\t  Sale Invoice\n")
            file.write("-------------------------------------------\n")
            file.write("Customer Name: " + name + "\n")
            file.write("Phone Number: " + str(phonenumber) + "\n")
            file.write("Address: " + address + "\n")

            #writing current year month day hour minute and second
            file.write("Date: " + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "\n")

            #creating a new invoiceid using name and timing unique value
            invoice_id = name + "_" + timing
            file.write("Invoice ID: " + invoice_id + "\n")
            file.write("\n-------------------------------------------\n")

            #looping through each items and printing the details
            for item in invoice_items:
                file.write("\nProduct Type: " + item['type'] + "\n")
                file.write("Brand Name: " + item['brand'] + "\n")
                file.write("Quantity Sold: " + str(item['quantity']) + "\n")

                #checking if any free items, if yes write the amount of free items
                if item['free_items'] > 0:
                    file.write("Free Items: " + str(item['free_items']) + "\n")
                file.write("Price: Rs. " + str(item['price']) + "\n")
                file.write("-------------------------------------------\n")

            file.write("TOTAL AMOUNT: Rs. " + str(total_price) + "\n")
            file.write("===========================================\n")
            file.write("Thank you for shopping with us. Hope you have a great day!\n")
            file.write("\nWe Care Store")

            #message to inform an invoice has been created 
            print("\nSale invoice generated successfully: " + filename)
