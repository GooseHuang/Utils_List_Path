import os
import glob
import datetime
import time

print('\n')

for x in glob.glob('./*'):
    x = os.path.abspath(x)
    x = x.replace('\\', '/')
    base_name = os.path.basename(x)

    print(x)


time.sleep(30)