import requests
import os

url = "https://www.stikombanyuwangi.ac.id/Home/kabar_berita";

response = requests.get(url);
html_content = response.text;

print(html_content);

# Create Folder
def CreateDirectory(namaFolder):
    if not os.path.exists(namaFolder):
        os.mkdir(namaFolder)

CreateDirectory("FolderScrap")

# Create File
def CreateNewFile(path):
    f = open(path, "w")
    f.write("")
    f.close()

CreateNewFile("FolderScrap/test.txt")

# Write File
def WriteFile(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")

WriteFile("FolderScrap/test.txt", "Ini merupakan isi dari file yang dibuat")

# Read File
def ReadFile(path):
    with open(path, "rt") as file:
        for line in file:
            print(line)

ReadFile("FolderScrap/test.txt")

# Validasi File
def FileExist(path):
    	return os.path.isfile(path);

print(FileExist("FolderScrap/test.txt"));

# # Hapus isi File
# def ClearFile(path):
#     f = open(path, "w");
#     f.close();

# ClearFile("FolderScrap/test.txt");
