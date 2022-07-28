import os
import shutil

extensions = {
    ".xlsx" : "Spreadsheets",
    ".exe" : "Setup Files",
    ".png" : "Images",
    ".jpeg" : "Images",
    ".jpg" : "Images",
    ".svg" : "Images",
    ".txt" : "Text",
    ".zip" : "Zip"
}

downlaodFolderPath = 'C:/Users/Muhammad Umair Khan/Downloads'

def checkFiles():
    availableFiles = os.listdir(downlaodFolderPath)
    return len(availableFiles), availableFiles
    
def getFileName(dir):
    exts = []
    for files in dir:
        ext = os.path.splitext(files)
        exts.append(ext[1])
    createFolders(exts)
            
def createFolders(exts):
    folder = set(exts)
    for x in folder:
        if x not in extensions.keys():
            fpath = os.path.join(downlaodFolderPath, "Misc")
        else:
            fpath = os.path.join(downlaodFolderPath, extensions[x])

        if not os.path.exists(fpath):
            os.mkdir(fpath)



dir = checkFiles()

getFileName(dir[1])