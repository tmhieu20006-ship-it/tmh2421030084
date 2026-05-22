n = int(input("Nhap n (0 < n < 100): "))

while n <= 0 or n >= 100:
    n = int(input("Nhap lai n: "))

tong = 0

for i in range(n):
    x = int(input(f"x[{i}] = "))

    # Kiem tra so nguyen to
    if x > 1:
        prime = True

        for j in range(2, int(x**0.5) + 1):
            if x % j == 0:
                prime = False
                break

        if prime:
            tong += x

print("Tong cac so nguyen to =", tong)

# Kiem tra dieu kien
if tong % 2 != 0 and tong > 50:
    print("Tong la so le va lon hon 50")
else:
    print("Tong khong thoa man dieu kien")