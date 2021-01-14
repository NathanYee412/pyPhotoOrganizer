import os
import datetime
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import *


# Sort a directory by creating folders based on file creation date
def sortFiles(base_path):
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

# chose a file path using tkinter filedialog
def selectDirectory():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)
    print(folder_selected)






if __name__ == "__main__":

    # GUI implementation
    window = Tk()
    window.geometry("600x600")

    folderPath = StringVar()

    chooseDir = tk.Button(window, pady=10, text="Choose the directory to organize.", command=lambda : selectDirectory())
    chooseDir.pack()

    orgButton = tk.Button(window, pady=10, text="Organize", command=lambda: sortFiles(str(folderPath.get())))
    orgButton.pack()

    # sortFiles(r'C:\Users\nyee\Desktop\testphotodir')
    window.mainloop()