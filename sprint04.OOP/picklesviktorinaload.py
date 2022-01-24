import pickle
import shelve
f = open("picklesviktorina.dat", "rb")
records = pickle.load(f)
print(records)