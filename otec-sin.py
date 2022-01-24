"""programma otec i sin"""
father_son = {"andriy": "roman", "igor": "viktor", "ivanka": "roman", "taras": "oleg"}
print("""
1.Enter father of son
2.Add
3.change
4.delete""")
vibor = input("chto vubiraem:  ")
if vibor == "1":
    name = input("vvedi nazvu sina :")
    if name in father_son:
        print(f"the father of {name} is {father_son[name]}")
    else:
        print(f"'{name}' is not in the son_father")
elif vibor == "2":
    sin = input("vvedite imya sina: ")
    father = input("vvedite imya bati: ")
    father_son[sin] = father
    print(father_son)
elif vibor == "3":
    name = input("vvedite imya")
    if name in father_son:
        father = input("izmenite otca na: ")
        father_son[name] = father
        print(father_son)
    else:
        print(f"zdes net sina po imeni {name}")
elif vibor == "4":
    name = input("vvedite imya kotore hotite udalit: ")
    if name in father_son:
        father_son.pop(name)
        print(father_son)
    else:
        print("Zdes net takogo imeni")
else:
    print("no option more than 4")

