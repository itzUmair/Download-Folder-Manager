import os

extensions = {
    "xlsx" : "Spreadsheets",
    "exe" : "Setup Files",
    "png" : "Images",
    "jpeg" : "Images",
    "jpg" : "Images",
    "svg" : "Images",
}

downlaodFolderPath = 'C:/Users/Muhammad Umair Khan/Downloads'

def checkFiles():
    availableFiles = os.listdir(downlaodFolderPath)
    return len(availableFiles), availableFiles
    
def getFileName(dir):
    folder = []
    for files in dir:
        fileExt = files.split(".")  
        folder.append(fileExt)      
    return folder
        
            
def createFolders(ext):
    folder = set(ext)
    print(folder) 

dir = checkFiles()
ext = getFileName(dir[1])
print(ext)