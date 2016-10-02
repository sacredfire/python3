import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Mac OS X and Linux:
source = ['/Users/Sergei_KIssel/Dropbox/DOCS']

# Notice we have to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Mac OS X and Linux:
target_dir = '/Users/Sergei_KIssel/python3/backup_DOCS'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# Notice the use of the os.sep variable - this gives the directory
# separator according to your operating system

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running..')
if os.system(zip_command) == 0:
    print('Success!')
else:
    print('Backup FAILED!')
