import os
import time

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

zip_command = "zip -r {} {}".format(target, source)

print("Zip commant is: \n{}".format(zip_command))

print('Running..')
if os.system(zip_command) == 0:
    print('Success!')
else:
    print('Backup FAILED!')
