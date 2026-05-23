f = open("e:\\matran.txt", "r")
 f = open("e:\\matran.txt", "r")
ma = [dong.split() for dong in f]   # ✅ Removed leading space
print(ma)
 
s = 0
for dong in ma:                      # ✅ Removed leading space
    for gia_tri in dong:
        s = s + float(gia_tri)
 
print("Tổng ma trận là:", s)         # ✅ Removed leading space
f.close()                            # ✅ Removed leading spacema = [dong.split() for dong in f]