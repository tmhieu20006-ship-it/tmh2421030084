x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
z = int(input("Nhap z: "))

tich = x * y * z

print("Tich =", tich)

# Dem so chu so
so_chu_so = len(str(tich))

# Tim chu so lon nhat
temp = tich
max_digit = 0

while temp > 0:
    digit = temp % 10

    if digit > max_digit:
        max_digit = digit

    temp //= 10

print("So chu so =", so_chu_so)
print("Chu so lon nhat =", max_digit)