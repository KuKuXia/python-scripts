import os
from zipfile import ZipFile

from datetime import datetime

# set file name and time of creation
today = datetime.now()
file_name = 'zipper_' + today.strftime('%Y.%m.%dh%H%M') + '.zip'
dir_name = './data/'  # update path


def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))


if __name__ == '__main__':
    zipfile = ZipFile(file_name, 'w')
    zipdir(dir_name, zipfile)
    zipfile.close()
