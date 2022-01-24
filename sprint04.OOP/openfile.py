x = open("read.it.txt", "r", encoding="utf-8")
z = x.read()
z = z.replace("i", "o")
print(z)


