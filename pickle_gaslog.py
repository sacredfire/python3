import os
import time
import pickle


sourcefile = '/Users/Sergei_KIssel/Dropbox/DOCS/gas_log.txt'
targetdir = '/Users/Sergei_KIssel/Dropbox/DOCS/'
targetfile = targetdir + os.sep + 'gas_log' + time.strftime('%Y%m%d') + '.data'

f = open(sourcefile, 'r')
data = f.read()
f.close()

f1 = open(targetfile, 'wb')
pickle.dump(data, f1)
f1.close()

# del data

# f1 = open(targetfile, 'rb')
# stored_data = pickle.load(f1)

# print(stored_data)
