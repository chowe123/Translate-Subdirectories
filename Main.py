from googletrans import Translator
from pathlib import Path
import os


translator = Translator()

def translate(s):
    """
    Translates s through google translate detect language
    """
    return translator.translate(s).text


def getListOfFiles(dirName):
    """
    Returns a list of all folders and files in their subdirectories
    """
    listOfFile = os.listdir(dirName)
    print(listOfFile)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles.append(fullPath)
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)          
    return allFiles

def TranslateNames(d):
    """
    Renames all files, folders and sub files and folders to their english equivilant through google translate
    """
    files = getListOfFiles(d)
    files.reverse()
    for file in files:
        basepath = os.path.basename(file)
        name = translate(Path(basepath).resolve().stem) + Path(basepath).suffix
        newpath = file.rsplit('\\', 1)[0] + '\\' + name
        os.rename(file, newpath)
        
        

# Example:
# filepath = ''   
# x = TranslateNames(filepath)
