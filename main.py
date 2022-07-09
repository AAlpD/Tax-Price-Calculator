lower = int(input("lower limit >> "))
upper = int(input("upper limit >> "))
o = int(input("tax rate >> "))
frequency = int(input("fiyat sıklığını giriniz(tavsiye edilen 100) >> "))
print("")


def cal_tax(l, u, tax, f):
    for i in range(l, u+1, f):
        normal_prize = int((i*100/(100+tax))*100/118)
        print(f"Normal prize: {normal_prize} USD Sale prize: {i} USD")


cal_tax(lower, upper, o, frequency)

input()
