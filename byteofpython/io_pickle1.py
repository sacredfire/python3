import pickle

shoplistfile1 = 'shoplist1.data'
shoplist = ['apple', 'mango', 'tickets', 'beer']

f = open(shoplistfile1, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile1, 'rb')
storedlist = pickle.load(f)

print(storedlist)
