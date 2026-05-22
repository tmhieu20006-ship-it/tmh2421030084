# khai báo một mảng
fruit = ["apple", "banana", "cherry"]      # ✅ No extra indent

for i in fruit:
    if i == "banana":
        continue    # ✅ Indented inside 'if' block
    print(i)        # ✅ At same level as 'if' (inside 'for')