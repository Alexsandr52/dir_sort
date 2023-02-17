import __init__ as init_modul
from pathlib import Path
from pprint import pprint

# cmd_list = [init_modul.get_file_by_extension('zip', like=False), init_modul.file_copy_in_dir(file_list, path=None, delet_first=False)]

help = ''' 
        group file copying
        get file by extension [1]
        file copy in dir [2]
        read config [3]
        write config [4]
        help [5]
    '''
print(help)
while True:
    
    cmd = input('>')
    if cmd in ['1', '2', '3', '4', '5', '0']:
        if cmd == '1':
            extension = input('Entr file extension like [txt]: ')
            like = True if 'y' in input('Do you want file with extension like your [doc, docx, ets], [y/n]: ') else False
            path = input('Input path or Enter to use default path: ')
            if path == '': path = None
            elif not Path(path).is_dir(): print(f'{path} doesn\'t exist'); continue
            try:
                file_list = init_modul.get_file_by_extension(extension, like=like, path=path)
                for i, file in enumerate(file_list):
                    print(f'{i}: {file}')
            except:
                print('We got problems sorry')

        if cmd == '2':
            extension = input('Entr file extension like [txt]: ')
            like = True if 'y' in input('Do you want file with extension like your [doc, docx, ets], [y/n]: ') else False
            delet_first = True if 'y' in input('Do you want delete sourse files [y/n]: ') else False
            sorse_path = input('Input sours path or Enter to use default path: ')
            out_path = input('Input out path or Enter to use default path: ')
            if sorse_path == '': sorse_path = None
            if out_path == '': out_path = None
            elif not Path(sorse_path).is_dir() or not Path(out_path).is_dir(): print(f'{path} doesn\'t exist'); continue
            try:
                file_list = init_modul.get_file_by_extension(extension, like=like, path=path)
                for i, file in enumerate(file_list):
                    print(f'{i}: {file}')
                print('files that you select:')
                if 'y' in input('Continue? [y/n]: '): 
                    init_modul.file_copy_in_dir(init_modul.get_file_by_extension(extension, like=like, path=sorse_path), path=out_path, delet_first=delet_first)
                else: 
                    continue
            except:
                print('We got problems sorry')

        if cmd == '3':
            pprint(init_modul.read_config(init_modul.main_path))
        
        if cmd == '3':
            configs = init_modul.read_config(init_modul.main_path)
            pprint(configs)
            param = configs.keys()
            print('TODO')

        if cmd == '5': print(help)
        if cmd == '0': print('GOODBY'); break
    elif cmd == '':
        continue
    else:
        print('incorrect')
        continue
    