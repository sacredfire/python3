import os
import time

source = '/Users/Sergei_KIssel/Dropbox/DOCS'

target_dir = '/Users/Sergei_KIssel/python3/backup_DOCS'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# The current day will be the name of the subdirectory in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')

# The current time will be the name of the zip archive.
now = time.strftime('%H%M%S')

# The name of the zip file
target = today + os.sep + now + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created dir', today)

# We use the zip command to put the files in a zip archive
zip_command = "zip -r {} {}".format(target, source)

# Run the backup
print("Zip commant is: \n{}".format(zip_command))

print('Running..')
if os.system(zip_command) == 0:
    print('Success!')
else:
    print('Backup FAILED!')
