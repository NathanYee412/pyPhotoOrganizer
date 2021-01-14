import os
import datetime
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox



# Sort a directory by creating folders based on file creation date
def setKeyValue(base_path):
    basepath = base_path
    filedate = {}

    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                filedate[entry.name] = datetime.datetime.fromtimestamp(entry.stat().st_ctime)
            
            # create folder name using file creation date
            foldername = str(filedate[entry.name])

            if not os.path.exists(base_path+'/'+foldername[:10]):
                
                # create a directory using the basepath and foldername 
                os.makedirs(base_path+'/'+foldername[:10])
                shutil.move(base_path+'/'+entry.name, base_path+'/'+foldername[:10]+'/'+entry.name)
            else:
                shutil.move(base_path+'/'+entry.name, base_path+'/'+foldername[:10]+'/'+entry.name)

# GUI implementation
window = tk.Tk(className="FileOrganizer")



if __name__ == "__main__":
    mykv = setKeyValue(r'C:\Users\nyee\Desktop\testphotodir')
