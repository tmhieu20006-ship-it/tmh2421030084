n = int(input("Nhập số nguyên dương n: "))

tich = 1
temp = n

while temp > 0:
    tich *= temp % 10
    temp //= 10

print("Tích các chữ số =", tich)

if tich % 2 == 0 and tich > 20:
    print("Tích là số chẵn và lớn hơn 20")
else:
    print("Không thỏa điều kiện")