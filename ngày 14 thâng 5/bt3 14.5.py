a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

# Tim chu so nho nhat cua b
temp = b
min_digit = 9

while temp > 0:
    digit = temp % 10

    if digit < min_digit:
        min_digit = digit

    temp //= 10

print("Chu so nho nhat cua b la:", min_digit)

# Kiem tra chia het
if min_digit != 0 and a % min_digit == 0:
    print(a, "chia het cho", min_digit)
else:
    print(a, "khong chia het cho", min_digit)