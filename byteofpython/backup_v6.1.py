import os
import time
import zipfile

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

# Choose compression mode
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = {zipfile.ZIP_DEFLATED: 'deflated',
         zipfile.ZIP_STORED: 'stored'}


# Define recursive zip
def recursive_zip(zf, source_file_path, archived_file_path):

    for root, dirs, files in os.walk(source):
        for file in files:
            zf.write(os.path.join(root, file), compress_type=compression)
            # ZipFile.write(filename, arcname=None, compress_type=None)

try:
    print('adding files from {} with compression mode {}'.format(
          source, modes[compression]))

# This is a check not to execute *.py files ???
    if __name__ == '__main__':

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
