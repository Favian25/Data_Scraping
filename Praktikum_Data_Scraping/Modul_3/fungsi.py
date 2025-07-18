import os

def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        
def create_new_file(path):
    f = open(path, 'w')
    f.write("")
    f.close()

def write_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        
def does_file_exist(path):
    return os.path.isfile(path)