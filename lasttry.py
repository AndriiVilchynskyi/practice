import random

# pir1 = "s sirom"
# pir2 = "s myasom"
# pir3 = "s djemom"
# pir4 = "s kapustoi"
# pir5 = "idi nahuj"
# a = [pir1, pir2, pir3, pir4 ,pir5]
# x = random.randrange(5)
# f =a[x]
# print(f)
# orel = 0
# reshka = 0
# count = 0
# while count <100:
#     x = random.randrange(2)
#     if x == 0:
#         reshka +=1
#     else:
#         orel +=1
#     count +=1
#
# print(orel, reshka)

# the_number = random.randint(1, 100)
# tries = 0
# guess = int(input("vvedite celoe chuslo: "))
# while guess != the_number and tries < 10:
#
#     if guess < the_number:
#         print("vvedite chislo pobolshe")
#     elif guess > the_number:
#         print("vvedite chislo pomen`she")
#     tries += 1
#     guess = int(input("vvedite celoe chuslo: "))
#
# if tries == 10:
#     print("poshel nahuj otsyuda, dolboeb")
# else:
#     print(f"konec igri,vu ugadali s  {tries}  raza")

#
a = 60
computer_guess = random.randint(1,100)
tries = 0
while computer_guess != a:
    if a > computer_guess:
        computer_guess = random.randint(computer_guess, 100)
    else:
        computer_guess = random.randint(1,computer_guess-1)
    tries +=1

print(f"computer ugadal s {tries} raza")
