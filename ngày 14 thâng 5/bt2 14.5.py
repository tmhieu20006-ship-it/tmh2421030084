n = int(input("Nhap n (0 < n < 200): "))

while n <= 0 or n >= 200:
    n = int(input("Nhap lai n: "))

tong = 0

for i in range(n):
    x = int(input(f"x[{i}] = "))

    # Kiem tra so chan
    if x % 2 == 0:
        tong += x

print("Tong cac phan tu chan =", tong)

# Kiem tra dieu kien
if tong % 7 == 0 and tong < 200:
    print("Tong chia het cho 7 va nho hon 200")
else:
    print("Tong khong thoa man dieu kien")