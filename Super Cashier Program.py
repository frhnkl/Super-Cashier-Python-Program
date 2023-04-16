#import required libraries 
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import text


#we start by creating class for transactions

class Transaction:
    def __init__(self): #this is for initialization
        self.items = []
        
    def add_item(self, item): #this is a functionfor adding an item
        self.items.append(item)
        
    def update_item_name(self, old_name, new_name): #this is a function for updating an item if we want to change what we bought
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name
    
    def update_item_qty(self, item_name, new_qty): #this is a function for updating the quantity of an item that we want to change
        for item in self.items:
            if item[0] == item_name:
                item[1] = new_qty
                1
    def update_item_price(self, item_name, new_price): #this is a function for updating the price of an item that we want to chang
        for item in self.items:
            if item[0] == item_name:
                item[2] = new_price
                
    def delete_item(self, item_name): #it's a functio for deleting items in the cart
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                
    def reset_transaction(self): #a function for resetting the transaction back to the original state (0)
        for item in self.items:
            self.items.remove(item)
    def check_order(self): #a function for checking what's inside the shopping cart
        try:
            total_price = 0
            print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
            print("|----|-----------|-------------|------------|-------------|")
            for i, item in enumerate(self.items):
                no = i+1
                name, qty, price = item
                total = qty * price
                total_price += total
                print(f"| {no:<2} | {name:<9} | {qty:<11} | {price:<10} | {total:<11} |")
            print("Pemesanan sudah benar")
        except:
            print("Terdapat kesalahan input data")
    
    def check_out(self): #this is a function for check out with added discounts for specific prices if total price meets minimum price for discount
        try:
            total_price = 0
            for item in self.items:
                name, qty, price = item
                total_price += qty * price
            if total_price >= 500000:
                discount = 0.07
            elif total_price >= 300000:
                discount = 0.06
            elif total_price >= 200000:
                discount = 0.05
            else:
                discount = 0
            total_price_after_discount = total_price * (1 - discount)
            print(f"barang yang dibeli: {self.items}")
            print(f"Total harga: {total_price}")
            print(f"Diskon: {discount*100}%")
            print(f"Harga setelah diskon: {total_price_after_discount}")
            print("Pembayaran sebesar ", total_price_after_discount, "telah berhasil dilakukan")           
            for item in self.items:
                name, qty, price = item
                self.insert_to_table(name, qty, price,  total_price, discount, total_price_after_discount)
            self.reset_transaction()
        except Exception as e:
            print(e)
            
    def insert_to_table(self, name, qty, price, total_price, discount, total_price_after_discount): #this is a function to store transactions results in a table
        conn = sqlite3.connect('transactions.db') #transaction results are stored in a file named transactions.db
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS transactions
                     (no_id INTEGER PRIMARY KEY ,
                      nama_item TEXT,
                      jumlah_item INT,
                      Price INT,
                      total_harga INT,
                      discount FLOAT,
                      harga_diskon INT)''')
        c.execute('INSERT INTO transactions (nama_item, jumlah_item, Price, total_harga, discount, harga_diskon) VALUES (?, ?, ?, ?, ?, ?)', (name, qty, price, total_price, discount, total_price_after_discount))
        conn.commit()
        
        
engine = create_engine('sqlite:///transactions.db') #start the engine for sqlite

conn = engine.connect() #connecting to sqlite


# create a new transaction

transaction =   Transaction()

# display the menu
print("Menu:")
print("1. Add item")
print("2. Update item name")
print("3. Update item quantity")
print("4. Update item price")
print("5. Delete item")
print("6. Check order")
print("7. Check out")
print("8. Reset transaction")
print("9. Exit")

# start the interaction loop
while True:
    # ask for user input
    choice = input("Choose an option: ")
    
    # execute the selected option
    if choice == "1":
        name = input("Enter item name: ")
        qty = int(input("Enter item quantity: "))
        price = int(input("Enter item price: "))
        transaction.add_item((name, qty, price))
        print(f"{name} has been added to the transaction.")
    elif choice == "2":
        old_name = input("Enter the old item name: ")
        new_name = input("Enter the new item name: ")
        transaction.update_item_name(old_name, new_name)
        print(f"{old_name} has been renamed to {new_name}.")
    elif choice == "3":
        name = input("Enter the item name: ")
        new_qty = int(input("Enter the new item quantity: "))
        transaction.update_item_qty(name, new_qty)
        print(f"{name} quantity has been updated to {new_qty}.")
    elif choice == "4":
        name = input("Enter the item name: ")
        new_price = int(input("Enter the new item price: "))
        transaction.update_item_price(name, new_price)
        print(f"{name} price has been updated to {new_price}.")
    elif choice == "5":
        name = input("Enter the item name: ")
        transaction.delete_item(name)
        print(f"{name} has been removed from the transaction.")
    elif choice == "6":
        transaction.check_order()
    elif choice == "7":
        transaction.check_out()
        print("Transaction has been completed.")
    elif choice == "8":
        transaction.reset_transaction()
        print("transaction has been resetted.")
    elif choice == "9":
        break
    else:
        print("Invalid option. Please try again.")

conn.close() #close the connection
