import os

def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)

def create_file(directory, filename, isiFile):
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(isiFile)

for data in range(5):
    dir_name = f"Directory_{data+1}"
    create_directory(dir_name)
    for j in range(5):
        create_file(dir_name, f"file ke-{j+1}.txt", f"Ini adalah isi file {j+1} di {dir_name}")