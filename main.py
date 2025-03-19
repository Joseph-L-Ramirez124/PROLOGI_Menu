from funcs import *  # Importing functions
from formats import *  # Importing formats
import os

menu_ui()
customer_order = []  # Initializing List
while True:  # Taking customer order
    order = input("").upper()
    if order == "END":
        break
    customer_order.append(order)  # Adds customer order to list
    os.system('cls')  # Resetting terminal
    mod_menu(customer_order)  # Shows modified menu with ordered items on the right-hand side

os.system('cls')  # Resetting terminal
cus_mode = input("Customer Discount (PWD and Senior only accepted): ").upper()
os.system('cls')  # Resetting terminal

receipt(customer_order, cus_mode)  # Receipt proper heading
burger_r(customer_order)  # burger row
fries_r(customer_order)  # fries row
soda_r(customer_order)  # soda row
receipt_discount(customer_order, cus_mode)  # discount row
