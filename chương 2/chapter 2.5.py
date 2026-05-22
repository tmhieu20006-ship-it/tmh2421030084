i = 1
while i <= 10:
    if i % 2 == 0:    # ✅ Indented inside while loop
        pass   
    else:
        print(i)      # ✅ Indented inside else block
    i += 1        