import pickle

# The name of the file where we will store the object
shoplistfile = 'phoplist.data'
# List of things to buy
shoplist = ['potato', 'onion', 'gasoline']

# Write to file
f = open(shoplistfile, 'wb')
# Dump object to file
pickle.dump(shoplist, f)
f.close()

# Destroy shoplist var
del shoplist

# Read from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)

print(storedlist)
