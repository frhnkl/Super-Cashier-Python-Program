### Super-Cashier-Python-Program


### Background 
Andi is the owner of a large supermarket in a city in Indonesia. Andi has plans to improve business processes, namely Andi will build a self-service cashier system at his supermarket with hope that:

• Customers can directly enter the items purchased, the number of items purchased, and the price of the items purchased and other features.

• Customers who are not in the city can buy goods from the supermarket.

### Requirements
there are also requirements from client which are:

1.	Customer can create a transaction ID
2.	Customer can add item, quantity of an item, and its price
3.	 If there are errors in the input, customer can change the item, quantity, and its price
4.	Customer can delete items in the shopping cart
5.	Customer can delete all transaction by using reset_transaction
6.	Customer can check what’s inside the shopping cart by using check_order()
7.	After that, the customer can self-check-out using check_out  metode but there are more requirements:

       a.	If total price > 200.000 customer gets 5% discount.
  
       b.	If total price > 300.000 customer gets 6% discount.
  
       c.	If total price > 500.000 customer gets 7% discount.
  
8.	Every time check_out method is run, transaction data will be imputed to data base in transaction table with insert_to_table(<source_data>)  function.
  a.	Columns that will be stored in the database are :
  
      i.	no_id
      
      ii.	nama_item
      
      iii.	jumlah_item
      
      iv.	price
      
      v.	total_harga
      
      vi.	harga_diskon
 
 ### Objectives
 program objectives:
 
 1. create a program where user can add their own item, quantity, price
 2. user can modify (update, delete, reset) their cart in that program
 3. user can check what's inside their shopping cart by using check_order ()
 4. user can self-check-out their own cart with 5% discount if total price is > 200.000, 6% discount if total price > 300.000, and 7% discount if total price > 500.000
 5. all transaction in check_out() will be stored in database (transactions.db file)

### Flowchart
![flowchart](https://user-images.githubusercontent.com/125452431/232310150-5f861a9b-92f6-4f1f-a07f-056ea49045df.jpg)

this is the flowchart of the generated code.
start : initializing ==> print menu: an interactive menu will be displayed along with a description of each option that can be taken ==> options consisting of 1 - 9 will be displayed. options 1 - 8 will execute the choice that the user will take and will display a display message from that choice. option 9 will 'break' and exit the loop 
==> the program will execute the selected option ==> continue returns to the selected loop or break ==> break loops.

### Function explanations
This code contains a Python class Transaction that handles transactions for a shopping cart. It has functions that add, update, delete items, as well as check orders and checkout. The transactions are stored in an SQLite database.

First, the code imports the required libraries sqlite3 and create_engine from sqlalchemy.

Then, the Transaction class is defined with the following functions:

__init__(self): Initializes the class by creating an empty list items.

add_item(self, item): Adds an item to the items list.

update_item_name(self, old_name, new_name): Updates the name of an item in the items list.

update_item_qty(self, item_name, new_qty): Updates the quantity of an item in the items list.

update_item_price(self, item_name, new_price): Updates the price of an item in the items list.

delete_item(self, item_name): Deletes an item from the items list.

reset_transaction(self): Resets the transaction back to the original state (empty items list).

check_order(self): Displays the items in the items list, along with their quantity, price, and total price.

check_out(self): Calculates the total price of the items in the items list, applies a discount if the total price meets certain criteria, displays the total price after discount, and stores the transaction in an SQLite database.

insert_to_table(self, name, qty, price, total_price, discount, total_price_after_discount): Inserts a transaction into an SQLite database.
Next, the code creates an engine for SQLite, and connects to it.

Then, it creates an instance of the Transaction class named transaction. After that, the code displays a menu and starts a loop that asks for user input and executes the corresponding function from the Transaction class.
The functions that can be called from the menu are:

add_item: Adds an item to the transaction.

```python
    def __init__(self): #this is for initialization
        self.items = []
```

update_item_name: Updates the name of an item in the transaction.
```python
 def update_item_name(self, old_name, new_name): #this is a function for updating an item if we want to change what we bought
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name
```
update_item_qty: Updates the quantity of an item in the transaction.
```
 def update_item_qty(self, item_name, new_qty): #this is a function for updating the quantity of an item that we want to change
        for item in self.items:
            if item[0] == item_name:
                item[1] = new_qty
```

update_item_price: Updates the price of an item in the transaction.
``` python
 def update_item_price(self, item_name, new_price): #this is a function for updating the price of an item that we want to chang
        for item in self.items:
            if item[0] == item_name:
                item[2] = new_price
```

delete_item: Deletes an item from the transaction.
``` python
def delete_item(self, item_name): #it's a functio for deleting items in the cart
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
```

check_order: Displays the items in the transaction, along with their quantity, price, and total price.
```python
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
```

check_out: Calculates the total price of the items in the transaction, applies a discount if the total price meets certain criteria, displays the total price after discount, and stores the transaction in an SQLite database.
``` python
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
```
reset_transaction: Resets the transaction back to the original state (empty transaction).
``` python
 def reset_transaction(self): #a function for resetting the transaction back to the original state (0)
        for item in self.items:
            self.items.remove(item)
```
exit: Exits the program.

### Code demonstration with test codes

### TEST 1
The customer wants to add two new items using the add_item() method. The items added are as follows: 

Item Name: Ayam Goreng, Qty: 2, Price: 20000

Item Name: Pasta Gigi, Qty: 3, Price: 15000

output: 
![Test 1](https://user-images.githubusercontent.com/125452431/232313997-9895cb80-ada4-4bfc-9a1c-55327606c869.jpg)

result in check_order

![Test 1 check order](https://user-images.githubusercontent.com/125452431/232314010-432aeb16-2605-4e56-968f-3ced67038748.jpg)

### TEST 2
It turns out that the customer bought the wrong item from the groceries that was added, so the customer uses the delete_item() method to delete the item. The item you want to delete is 'Pasta Gigi'.

output, we using menu '5' which is delete item:

![test 2](https://user-images.githubusercontent.com/125452431/232314204-5fba7b2b-6cf1-4b84-9130-5b9ab4ea821e.jpg)

as we can see in the check order, 'Pasta Gigi' has been removed.

![test 2 check order](https://user-images.githubusercontent.com/125452431/232314212-3f826373-2e0c-4de9-a8d3-c3a643dc56f7.jpg)

### TEST 3
It turns out that after thinking about it, the customer entered the wrong item he wanted to spend! Instead of deleting them one by one, 
the Customer can simply use the reset_transaction() method to delete all items that have been added.

output, we using menu '8' which is reset transaction:

![test 3](https://user-images.githubusercontent.com/125452431/232314404-fe9ac243-ba27-424d-803d-83fcf02395d7.jpg)


as we can see, all transaction has been resetted or deleted in the check order result:
![test 3 check order](https://user-images.githubusercontent.com/125452431/232314413-56ab670e-e72f-442f-a169-35b86b274d54.jpg)

### TEST 4
After the customer has finished shopping, he will calculate the total expenditure to be paid using the check_out() method. 
Before issuing the total shopping output, it will display the items purchased.

output: 

![test 4](https://user-images.githubusercontent.com/125452431/232314792-f91939f5-7806-4ac3-b9d7-52206984aa0d.jpg)

### TEST 5
testing for applied discount.

output :

![test 5](https://user-images.githubusercontent.com/125452431/232314916-275d1304-2227-45f4-b9e6-c81d4284492f.jpg)

as we can see, discount is implemented on items that reach it's threshold.

### CONCLUSION
The given code is a program that simulates a shopping cart transaction. It allows users to perform various actions such as adding, updating, and deleting items in the cart. The program also provides the user with the ability to check the order, calculate discounts, and store the transaction details in an SQLite database.

Overall, the given code provides a simple implementation of a shopping cart transaction system with the ability to store transaction details in an SQLite database. However, the code can be improved by adding more error handling and input validation to handle edge cases and prevent errors.
