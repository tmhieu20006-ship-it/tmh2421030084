a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

tong = a + b
print("Tổng =", tong)

max_digit = 0
temp = tong

while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    temp //= 10

print("Chữ số lớn nhất trong tổng là:", max_digit)