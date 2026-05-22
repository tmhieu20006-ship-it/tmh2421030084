a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

tong = a + b + c

print("Tong =", tong)

# Dem chu so chan
temp = tong
dem = 0

while temp > 0:
    digit = temp % 10

    if digit % 2 == 0:
        dem += 1

    temp //= 10

print("So chu so chan trong tong =", dem)