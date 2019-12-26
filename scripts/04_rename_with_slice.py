import glob
import os

DIR = "D:\\MyDownload\\"
EXTENSION = '*.ass'

os.chdir(DIR)
for file in glob.glob(EXTENSION):
    file_name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    file_name = file_name.split('.')[:3]

    new_file_name = '.'.join(file_name[:3]) + extension
    print(new_file_name)
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(e)
    else:
        print("Renamed {} to {}".format(file, new_file_name))
