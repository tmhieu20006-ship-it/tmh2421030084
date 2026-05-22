a = []
s= 0
n = int(input("Nhap mot phan tu cua day so: "))
for i in range(n):
    a.append(int(input("Nhap phan tu thu " + str(i+1) + ": ")))
    s += a[i]
print("Tong cac phan tu trong mang la:", s)