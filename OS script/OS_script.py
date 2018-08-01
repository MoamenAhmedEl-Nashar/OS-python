import os
import shutil
dir='C:\\Users\\merav\\Desktop\\newFolderCreatedByPython'
os.makedirs(dir,511,True)
lis=os.listdir('C:\\Users\\merav\\Desktop')
for i in lis:
    file='C:\\Users\\merav\\Desktop\\'+i
    shutil.move(file,dir)

