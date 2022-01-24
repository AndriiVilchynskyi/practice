import random
count = 0
words = ("ігор", "андрій", "катя", "діана", "влад")
word = random.choice(words)
a = len(word)
print(f"в слове есть {a} букв")
correct = ""
while count < 5:
    letter = input("угадайде букву в слове :")
    if letter in word:
        print("Да, есть такая буква")
    else:
        print("Нет такой буквы")
    count +=1

correct = input("введите слово полностю :")
if correct.lower() == word:
    print("Вы выиграли")
else:
    print("Вы проиграли")

