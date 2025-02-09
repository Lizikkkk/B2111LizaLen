def checker(var1):
    if type(var1) != str:
        raise TypeError(f"Ми не можемо працювати з цим типом данних - {type(var1)}. Потрібен тип - str!")
    else:
        return var1


my_var = 10
my_var2 = "Vasya"
checker(my_var)
checker(my_var2)