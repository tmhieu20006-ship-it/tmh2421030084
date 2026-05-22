m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

# Tinh tong
tong = m + n

print("Tong =", tong)

# Tim chu so lon nhat trong tong
temp = tong
max_digit = 0

while temp > 0:
    digit = temp % 10

    if digit > max_digit:
        max_digit = digit

    temp //= 10

print("Chu so lon nhat trong tong la:", max_digit)