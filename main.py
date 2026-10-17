#Racunarska firma projekat

from functions import add_product
from functions import inventory_overview
from functions import sell_product
from functions import product_search

# Pre glavnog menija, potrebno je ispisati upozorenje na nizak lager ukoliko je nizak, pa tek onda ispisati glavni meni
# Ukoliko nema niskog lagera, upozorenje se nece ispisivati i aplikacija ce odmah prikazati gavni meni
print("============ TECH INVENTORY APP ==============")
print("Options:")
print("Inventory Overview    -> press 1")
print("Add Product           -> press 2")
print("Sell Product          -> press 3")
print("Product Search        -> press 4")
print("Business Report       -> press 5")

option = input("Enter option: ")

if option == "1":
    print("\nID      PROIZVOD                        KOL.          CENA")
    print("-------------------------------------------------------------")
    inventory_overview()

elif option == "2":
    add_product()

elif option == "3":
    sell_product()

elif option == "4":
    product_search()

print("\n")

# Svaka prodaja mora da se upise u poseban sales.txt dokument!!!


# Ovo je BUSINESS REPORT koji mora da se prikaze ako korisnik odabere opciju 5
# print("============ BUSINESS REPORT ================ ")
# print(f"Total Number of Products: ")
# print(f"Total Items in Stock: ")
# print("\n")
# print(f"Total Inventory Value: RSD")
# print("\n")
# print(f"Total Sales: RSD")
# print("\n")
# print(f"Best-Selling Product: \n ")
# print("\n")
# print("Products with Low Stock: \n")