ch_1 = float(input("Print your num 1: "))
ch_2 = float(input("Print your num 2: "))
try:
    res = ch_1/ch_2
    print(res)
except:
    print(f"You try division {ch_1} by {ch_2} and it's error")
    if ch_2 == 0:
        print("By 0 division error")
else:
    print("End of program")