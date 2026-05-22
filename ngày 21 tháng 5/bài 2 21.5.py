n = int(input("Nhập số nguyên dương n: "))

tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

print("Tổng các chữ số =", tong)

if tong % 3 == 0:
    print("Tổng chia hết cho 3")
else:
    print("Tổng không chia hết cho 3")