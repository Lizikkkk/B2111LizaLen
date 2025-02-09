ch_1 = int(input("Напиши перше число, яке ділиться на 5: "))
ch_2 = int(input("Напиши друге число, яке ділиться на 5: "))
ch_3 = int(input("Напиши третє число, яке ділиться на 5: "))


def check (ch_1, ch_2, ch_3):
    if ch_1 % 5 == 0:
        if ch_2 % 5 == 0:
            if ch_3 % 5 == 0:
                sp = [ch_1, ch_2, ch_3]
                sp.sort()
                print(sp)
            else:
                raise TypeError(f"Число не правильне! {ch_3} не ділиться на 5!")
        else:
            raise TypeError(f"Число не правильне! {ch_2} не ділиться на 5!")
    else:
        raise TypeError(f"Число не правильне! {ch_1} не ділиться на 5!")


try:
    check(ch_1, ch_2, ch_3)
except TypeError:
    print("Введено не коректні числа!")
