import os
import datetime
import shutil

# print(entry.stat().st_ctime)
# print('time: ',datetime.datetime.fromtimestamp(entry.stat().st_ctime)  )


def setKeyValue(base_path):
    basepath = base_path
    filedate = {}

    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                filedate[entry.name] = datetime.datetime.fromtimestamp(entry.stat().st_ctime)

    return filedate

#print dictionary of files 
def printDict(myDict):
    for x in myDict:
        print(x, ' ', myDict[x])


def organizeFiles():
    for file_ in list_:
        name,ext = os.path.splitext(file_)
        print(name)
        #Stores the extension type
        ext = ext[1:]
        #If it is directory, it forces the next iteration
        if ext == '':
            continue
        #If a directory with the name 'ext' exists, it moves the file to that directory
        if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
        #If the directory does not exist, it creates a new directory
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)

if __name__ == "__main__":
    mykv = setKeyValue(r'C:\Users\nyee\Desktop\testphotodir')
    printDict(mykv)
