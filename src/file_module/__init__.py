from pathlib import Path  
import json
import glob
import shutil 
import os
import datetime

# read write definition  
main_path = 'src/file_module/config.json'
def read_config(main_path=main_path) -> dict:
    with open(main_path, 'r') as config_file: 
        configs = json.load(config_file)
        return configs

def write_config(main_path, new_configs) -> None:
    with open(main_path, 'w') as config_file: json.dump(new_configs, config_file)

def get_file_by_extension(extension, path=None, like=True) -> list():
    if path == None:
        with open(main_path) as config_file: 
            path =  json.load(config_file)['test_path']

    if like: return glob.glob(f'{path}/*{extension}*')        
    return glob.glob(f'{path}/*{extension}')

def file_copy_in_dir(file_list, path=None, delet_first=False):
    if path == None:
        filename, file_extension = os.path.splitext(file_list[0])
        with open(main_path) as config_file: 
            default_path =  json.load(config_file)['default_path']
        path = f'{default_path}/{file_extension}'
        try: os.mkdir(path)
        except: print(f'folder {path} already exist')

    for file in file_list:
        date, time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').split()
        time = time.replace(':','-')
        filename = f'{date}_{time}_{Path(file).name}'
        shutil.copy2(file, f'{path}/{filename}')
        if delet_first: os.remove(file)
    return True

if __name__ == '__main__':
    # reset to default sattings
    configs = {
        'default_path': 'output',
        'test_path': 'input',
        'same': False,
        'smart_name': True,
    }
    write_config(main_path, configs)
    print(read_config())
    for i in range(10):
        with open(f'input/{i}.txt', 'w'):
            continue
    # print(get_file_by_extension('txt'))
    # print(get_file_by_extension('txt', like=False))
    # file_copy_in_dir(get_file_by_extension('txt', like=True), delet_first=True)