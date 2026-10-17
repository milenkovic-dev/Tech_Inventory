import json

with open('products.json') as file:
    products = json.load(file)

#Funkcija za dodavanje proizvoda na lager
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


#Funkcija za pregled stanja
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
