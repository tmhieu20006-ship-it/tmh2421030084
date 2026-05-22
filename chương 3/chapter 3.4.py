fi = open("input.txt", "r", encoding="utf-8")
fchu = open("outchu.txt", "w", encoding="utf-8")
fso = open("outso.txt", "w", encoding="utf-8")

for line in fi.readlines():
    words = line.split()

    for w in words:
        if w.isdigit():
            fso.write(w + "\n")
        else:
            fchu.write(w + " ")

    fchu.write("\n")

fi.close()
fchu.close()
fso.close()
