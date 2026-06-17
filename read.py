""""
    This function reads product from a file named 'products.txt' that returns a list of products 
    like name, brand, quantity, selling price and country of origin. This function also generates a unique ID for each 
    product stored in a empty list called products[].
    
    Parameter: Takes the file_path declared in main module 'product.txt'
    Exception: FileNotFoundError raises if file path doesnt exist
    Returns:  [1, 'Watch', 'Swiss', 10, 10000.0, 'Nepal'],
"""
# Function to read product data
def read_products(file_path):
    products = [] #empty list to store product data 
    try:
        with open(file_path, 'r') as file:
            for line in file: #looping through each line
                parts = line.split(',') #splitting the line into different part using comma
                if len(parts) >= 5:
                    id_num = len(products) + 1 #automatically generated id
                    name = parts[0]
                    brand = parts[1]
                    quantity = int(parts[2])
                    cost_price = float(parts[3])
                    country = parts[4]

                    #increases selling_price by 200%
                    selling_price = cost_price * 3  
                    #adding value to the empty list 

                    product = [id_num, name, brand, quantity, selling_price, country]
                    products.append(product)
    except FileNotFoundError:
        print("File not found")

    return products