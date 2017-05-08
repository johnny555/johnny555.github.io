import os
from subprocess import call
import re

files = os.listdir('.')

filtered_files = []
for f in files:
    found = re.findall('[_-a-z0-9]*.png', f)
    if len(found) > 0:
        print(f)
        filtered_files.append(f)


for f in filtered_files:

    call(['convert', f, '-resize', '20%', f])
