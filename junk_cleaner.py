import os
import shutil



source_path = "c:/users/USER_NAME/Downloads/"

destination_path_screenshots = source_path + "ScreenShots/"

destination_path_cpp =  source_path + "cpp/"

destination_path_py = source_path + "py/"

if not os.path.isdir('new_folder'):
	if not os.path.exists(destination_path_screenshots):
		os.mkdir(destination_path_screenshots)
if not os.path.isdir('new_folder'):
	if not os.path.exists(destination_path_cpp):
		os.mkdir(destination_path_cpp)
		
if not os.path.isdir('new_folder'):
	if not os.path.exists(destination_path_py):
		os.mkdir(destination_path_py)


for file in os.listdir(source_path):
    
    filename = os.fsdecode(file)
     
    if filename.endswith(".cpp"):
     
        shutil.move(source_path + filename, destination_path_cpp + filename)
        continue
    if filename.endswith(".png"):
         
         if ("Screen Shot" in filename or "Screenshot" in filename):
         
            shutil.move(source_path + filename, destination_path_screenshots + filename)
               
            continue
        
    if filename.endswith(".py"):
     
        shutil.move(source_path + filename, destination_path_py + filename)
    

         