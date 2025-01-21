import os

def CreateDirectory(namaFolder):
    if not os.path.exists(namaFolder):
        os.makedirs(namaFolder);

def CreateNewFile(path):
    f = open(path, "w");
    f.write("");
    f.close();

def WriteToFile2(path, data, response):
    fullPath = os.path.join(path, data);
    with open(fullPath, 'wb') as f:
        f.write(response.content);

def ReadData(path):
    with open(path, "r") as file:
        for line in file:
            print(line.replace("\n", ""));

def ReadLines(path, lines):
    with open(path, "rt") as file:
        currLine = 0;
        for line in file:
            if currLine == lines:
                break;
            currLine += 1;
            print(line.replace("\n", ""));
            
def DoesFileExist(path):
    return os.path.isfile(path);