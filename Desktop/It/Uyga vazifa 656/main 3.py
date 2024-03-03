list = [1, 2, "13", "4", 5, "645"]
summa = 0
def numbers_sum(list, summa):
    for x in list:
        if type(x) == int:
            summa = summa + x

    return summa


print(numbers_sum(list, summa))