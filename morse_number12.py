def morse_number(num):
    res = ""
    for i in num:
        i = int(i)
        if i < 6:
            res += (5 * "-").replace("-", ".", i) + " "
        else:
            res += (5 * ".").replace(".", "-", i-5) + " "
        return res.rstrip()



a = morse_number("333")
print(a)