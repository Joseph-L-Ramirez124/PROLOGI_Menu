from funcs import *  #
import time


def menu_ui():  # Main menu
    print("|=================================================================================|")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|                                                                                 |")
    print("|=================================================================================|")
    return


def discount(item, mode="No Discount"):  # Discount screen
    if mode == "PWD":
        new_total = (price_total(item)-(price_total(item)*0.15))
        return new_total
    elif mode == "SENIOR":
        new_total = (price_total(item)-(price_total(item)*0.20))
        return new_total
    else:
        new_total = price_total(item)
        return new_total


def mod_menu(item):
    print("|================================================================================|")
    print("|                                                           |Current Order:      |")
    print("|                                                           |" + str(burger(item)) + "x Burgers          |")
    print("|                                                           |" + str(fries(item)) + "x Fries            |")
    print("|                                                           |" + str(soda(item)) + "x Sodas            |")
    print("|                                                           |                    |")
    print("|                                                           |Current Total:" + str(price_total(item))+"  |")
    print("|================================================================================|")
    return


def receipt(item, mode):  # Receipt header
    current_time = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", current_time)

    print("Jameson's Burgers, INC.")
    print(time_string)
    print("Taft Avenue, Manila City")
    print("===========================================================")
    print("Receipt Total . . . . . . . . . . . . . . . . . . PHP" + str(discount(item, mode)))
    print("===========================================================")
    print("QTY          ITEM            UNIT PRICE              AMOUNT")


def receipt_discount(item, mode="No Discount"):  # Receipt discount
    if mode == "PWD":
        print("PWD DISCOUNT . . . . . . . . . . . . . . . . . . . . PHP " + str(price_total(item)*0.15))
    elif mode == "SENIOR":
        print("SENIOR CITIZEN DISCOUNT . . . . . . . . . . . . . .  PHP " + str(price_total(item)*0.20))
    return
