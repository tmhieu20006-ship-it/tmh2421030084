n = int(input("Nhap n (0 < n < 100): "))

while n <= 0 or n >= 100:
    n = int(input("Nhap lai n: "))

tong = 0
dem = 0

for i in range(n):
    x = float(input(f"x[{i}] = "))

    if -1000 < x < -10:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print("Trung binh cong =", round(tbc, 2))
else:
    print("Khong co phan tu thoa man")