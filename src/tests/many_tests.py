import sys
import os
sys.path.append('src/file_module/')      
import __init__ as init_modul
import random

extensions = ['test', 'docxtest', 'lil', 'lost']
for i in range(100):
        with open(f'input/{i}.{random.choice(extensions)}', 'w'):
            continue

for extension in extensions:
    try: init_modul.get_file_by_extension(extension); print(True)
    except: print(False)

    try: init_modul.get_file_by_extension(extension, like=False); print(True)
    except: print(False)

    try: init_modul.file_copy_in_dir(init_modul.get_file_by_extension(extension, like=False), delet_first=True); print(True)
    except: print(False)

# for extension in extensions:
#     os.rmdir(f'output/.{extension}')