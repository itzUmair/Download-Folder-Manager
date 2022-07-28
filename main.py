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
    ".zip" : "Zip", 
    ".docx" : "Word",
    ".ppt" : "PowerPoint",
    ".pdf" : "PDF",
    ".msi" : "Setup Files"
}

downlaodFolderPath = 'C:/Users/Muhammad Umair Khan/Downloads'

def checkFiles():
    availableFiles = os.listdir(downlaodFolderPath)
    return len(availableFiles), availableFiles
    
def getFileNames(dir):
    exts = []
    for files in dir:
        ext = os.path.splitext(files)
        exts.append(ext[1])
    createFolders(exts)
    moveFile(dir, exts)
            
def createFolders(exts):
    folder = set(exts)
    for x in folder:
        if x not in extensions.keys():
            fpath = os.path.join(downlaodFolderPath, "Misc")
        else:
            fpath = os.path.join(downlaodFolderPath, extensions[x])

        if not os.path.exists(fpath):
            os.mkdir(fpath)

def moveFile(dir, exts):
    for files in dir:
        for ext in exts:
            if files.endswith(ext):
                if ext not in extensions.keys():
                    fpath = os.path.join(downlaodFolderPath , "Misc" , files)
                else:
                    fpath = os.path.join(downlaodFolderPath , extensions[ext] , files)
                    cpath = os.path.join(downlaodFolderPath , files)
                    print(cpath)
                    os.rename(cpath, fpath)
    

dir = checkFiles()

getFileNames(dir[1])
