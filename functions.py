import json

with open('products.json') as file:
    products = json.load(file)

# Function for Adding Product to Inventory
def add_product():
    with open("products.json", "r") as file:
        products = json.load(file)

    name = input("Input the name of the product: ")
    category = input("Input the category of the product: ")
    purchase_price = float(input("Input purchase price of the product: "))
    selling_price = float(input("Input selling price of the product: "))
    quantity = int(input("Input the quantity of the product: "))
    minimal_quantity = int(input("Input minimal quantity of the product: "))

    if products:
        new_id = max(product["id"] for product in products) + 1
    else:
        new_id = 1001

    new_product = {
        "id": new_id,
        "naziv": name,
        "kategorija": category,
        "nabavna_cena": purchase_price,
        "prodajna_cena": selling_price,
        "kolicina": quantity,
        "minimalna_kolicina": minimal_quantity
    }

    products.append(new_product)

    with open("products.json", "w") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)

    print(f"Proizvod '{name}' uspesno je dodat. ID: {new_id}")


# Function for Inventory Overview
def inventory_overview():
    with open("products.json", "r") as file:
        products = json.load(file)

    for product in products:
        cena = f"{product['prodajna_cena']:,.0f}".replace(",", ".")

        print(
            f"{product['id']:<8}"
            f"{product['naziv']:<32}"
            f"{product['kolicina']:<10}"
            f"{cena:>10}"
        )


# Function for Selling Products
def sell_product():
    with open("products.json", "r") as file:
        products = json.load(file)

    product_id = int(input("Enter product ID: "))
    sold_quantity = int(input("Enter quantity sold: "))

    if sold_quantity <= 0:
        print("Error: Quantity must be greater than zero.")
        return

    for product in products:
        if product["id"] == product_id:

            previous_stock = product["kolicina"]

            if sold_quantity > previous_stock:
                print("Error: Not enough products in stock.")
                return

            product["kolicina"] -= sold_quantity

            with open("products.json", "w") as file:
                json.dump(products, file, indent=4, ensure_ascii=False)

            print("\nSale completed successfully!")
            print(f"Product: {product['naziv']}")
            print(f"Previous stock: {previous_stock}")
            print(f"Sold: {sold_quantity}")
            print(f"New stock: {product['kolicina']}")

            return

    print("Error: Product not found.")


#Funkcija za Product Search
def product_search():
    with open("products.json", "r") as file:
        products = json.load(file)
        search = input("Enter product name, category, ID or price range: ").strip()

        results = []

    if "-" in search:
            min_price, max_price = search.split("-")
            min_price = float(min_price)
            max_price = float(max_price)

            for product in products:
                if min_price <= product["prodajna_cena"] <= max_price:
                    results.append(product)

    else:
            for product in products:
                if search.lower() in product["naziv"].lower():
                    results.append(product)

                elif search.lower() in product["kategorija"].lower():
                    results.append(product)

                elif search.isdigit() and product["id"] == int(search):
                    results.append(product)


    if results:
            print("\nSearch results:")
            print(f"{'ID':<8}{'PROIZVOD':<32}{'KOL.':<10}{'CENA':>10}")
            print("-" * 60)

            for product in results:
                price = f"{product['prodajna_cena']:,.0f}".replace(",", ".")

                print( f"{product['id']:<8}" 
                       f"{product['naziv']:<32}" 
                       f"{product['kolicina']:<10}" 
                       f"{price:>10}" )

    else: print("No products found.")