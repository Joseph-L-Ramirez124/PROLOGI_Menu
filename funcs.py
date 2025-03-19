
def burger(item):  # Counts how many burgers, int
    burger_list = [x for x in item if "BURGER" in x]
    burger_num = len(burger_list)
    return burger_num


def soda(item):  # Counts how many sodas, int
    soda_list = [y for y in item if "SODA" in y]
    soda_num = len(soda_list)
    return soda_num


def fries(item):  # Counts how many fries, int
    fries_list = [z for z in item if "FRIES" in z]
    fries_num = len(fries_list)
    return fries_num


def burger_total(item):  # Gives Burger total, int
    b_total = burger(item)*500
    return b_total


def soda_total(item):  # Gives Soda total, int
    s_total = soda(item)*80
    return s_total


def fries_total(item):  # Gives Fries total, int
    f_total = fries(item)*200
    return f_total


def price_total(item):  # Computes for the total price of items ordered, int
    c_total = (burger_total(item) + soda_total(item) + fries_total(item))
    return c_total


def burger_r(item):  # Checks if customer ordered burger, prints if true
    if burger(item) == 0:
        return
    else:
        print(str(burger(item)) + "x           BURGERS         PHP 500                 PHP " + str(burger_total(item)))
        return


def fries_r(item):  # Checks if customer ordered fries, prints if true
    if fries(item) == 0:
        return
    else:
        print(str(fries(item)) + "x           FRIES           PHP 200                 PHP " + str(fries_total(item)))
        return


def soda_r(item):  # Checks if customer ordered sodas, prints if true
    if soda(item) == 0:
        return
    else:
        print(str(soda(item)) + "x           SODA            PHP 80                  PHP " + str(soda_total(item)))
        return



