import os 
import shutil

path=input('name the directory to be sorted')
list=os.listdir(path)
for folder in list: 
    name=os.path.splitext(folder) 
    
  
    
    if os.path.exists(path):
        shutil.move(path+'/'+folder,path+'/'+folder)

        
    else:
        os.makedirs(path)
        shutil.move(path+'/'+folder,path+'/'+folder)
        
        
        
        
        #to arrange all the folders in an order. 
        