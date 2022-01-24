import shelve, pickle
print("Консервация списков ")
variety =["огурцы", "помидоры", "капуста"]
shape = ["целые" , "кубиками", "соломкой"]
brand = ["Главпродукт" , "Чумак", "Бондюзль"]

f = open("picklesl.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()
f = open("picklesl.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
