2.54
3.6
5.78
4.123
3.4
7.999
f = open("e:\\matran.txt", "r")
ma = []
ma = [dong.split() for dong in f]
print(ma)
s = 0
for subama in ma:
    for i in subama:
        s = s + float(i)
print("Tong cua ma tran la:", s)