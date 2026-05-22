m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

print("Tổng các chữ số của n =", tong)

if tong != 0 and m % tong == 0:
    print(m, "chia hết cho", tong)
else:
    print(m, "không chia hết cho", tong)