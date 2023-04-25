import os 
import shutil
import string
path = os.getcwd()
images_path = path+'/image'
video_path = path+'/videos'
documents_path = path+'/documents'
misc_path = path+'/miscellaneous'

files = os.listdir(path)
try:
  os.mkdir(images_path)
  os.mkdir(video_path)
  os.mkdir(documents_path)
  os.mkdir(misc_path)
except:
  print("files already created")

  
for file in files:
  if(os.path.isdir(file) == True):
    continue
  if (file.endswith(".png") == True or file.endswith(".jpg") == True):
   shutil.move(os.path.join(path, file),os.path.join( images_path, file))  
  elif(file.endswith(".pdf") == True):
    shutil.move(os.path.join(path, file),os.path.join( documents_path, file)) 
  elif(file.endswith('.mp4') == True):
    shutil.move(os.path.join(path, file),os.path.join( video_path, file)) 
  else:
    shutil.move(os.path.join(path, file),os.path.join( misc_path, file)) 
