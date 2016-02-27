import os
import time
# from zipfile_infolist import print_info
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

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = {zipfile.ZIP_DEFLATED: 'deflated',
         zipfile.ZIP_STORED: 'stored'}

print('Creating archive')
zf = zipfile.ZipFile(target, mode='w')
try:
    print('adding files from {} with compression mode {}'.format(
        source, modes[compression]))
    for filename in glob.glob(source + os.sep + '*'):
        zf.write(filename, os.path.basename(filename),
                 compress_type=compression)
finally:
    print('closing')
    zf.close()
