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
    ".docx" : "Word Document",
    ".ppt" : "PowerPoint",
    ".pdf" : "PDF",
    ".msi" : "Setup Files"
}

downlaodFolderPath = 'C:/Users/Muhammad Umair Khan/Downloads'

def checkFiles():
    # os.chdir(downlaodFolderPath)
    filesInDir = os.listdir(downlaodFolderPath)
    return filesInDir
    
def checkExtensions(dir):
    for files in dir:
        fileName, fileExt = os.path.splitext(files)
        if fileExt.startswith(".") and fileExt in extensions.keys():
            cpath = os.path.join(downlaodFolderPath, files)
            fpath = os.path.join(downlaodFolderPath, extensions[fileExt], files)
            os.rename(cpath, fpath)

        if fileExt.startswith(".") and fileExt not in extensions.keys():
            cpath = os.path.join(downlaodFolderPath, files)
            fpath = os.path.join(downlaodFolderPath, "Misc", files)
            os.rename(cpath, fpath)



def moveFile():
    pass

dir = checkFiles()
checkExtensions(dir)