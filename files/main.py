__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import zipfile

def clean_cache():
    new_folder = 'files\cache'
    if os.path.exists(new_folder):
        for file in os.listdir(new_folder):
            os.remove(os.path.join(new_folder, file))
        os.rmdir(new_folder)
    os.makedirs(new_folder)

def cache_zip(path_zip, path_dir):
    clean_cache()
    with zipfile.ZipFile(path_zip, 'r') as zip_ref:
        zip_ref.extractall(path_dir)

def cached_files():
    files = []
    for file in os.listdir('files\cache'):
        #print(file)
        files.append(os.path.abspath(os.path.join('files\cache',file)))
    return files

def find_password(files):
    passwords = []
    password =""
    for file in files:
        #print(file)
        with open(file) as f:
             lines = f.readlines()
             passwords.append(lines)
    for x in passwords:
        for y in x:
            if 'password' in y:
               password = y[y.find(": ")+2:-1] 
    return password
