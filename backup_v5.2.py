import os
import time
import zipfile
import glob

source = '/Users/Sergei_KIssel/Dropbox/DOCS'
target_dir = '/Users/Sergei_KIssel/python3/backup_DOCS'


if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Enter comment here:')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created dir "today"')

# Create archive file
print('creating archive..')
zf = zipfile.ZipFile(target, mode='w')

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = {zipfile.ZIP_DEFLATED: 'deflated',
         zipfile.ZIP_STORED: 'stored'}


def recursive_zip(zf, source, target_dir):

    for item in glob.glob(source + os.sep + '*'):

        if os.path.isfile(item):
            zf.write(item, os.path.basename(item), compress_type=compression)

        elif os.path.isdir(item):
            recursive_zip(zf, item, os.path.basename(item))

try:
    print('adding files from {} with compression mode {}'.format(
          source, modes[compression]))

# Calling the recursive_zip func defined above
    recursive_zip(zf, source, target_dir)

finally:
    print('closing')
    zf.close()

# Open zip to see what's in it
print('reading archive:')
zf = zipfile.ZipFile(target, mode='r')

for info in zf.infolist():
    print(info.filename, info.date_time, info.file_size, info.compress_size)
