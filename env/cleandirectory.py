import os
import shutil

sort_folder = "sorted"

def sort_in_folder(file, folder):
    if not os.path.exists(f"./{sort_folder}/{folder}"):
        create_subfolder(folder)

    print(f"moving {file} to {folder}")
    shutil.move(f"./{file}", f"./{sort_folder}/{folder}/{file}")

def create_subfolder(folder):
    print(f"created subfolder {folder}")
    os.mkdir(f"./{sort_folder}/{folder}")



# create a dict with all thet fileypes as keys
filetypes = {
    # Images
    ".png" : "Images",
    ".psd" : "Images",
    ".jpg" : "Images",
    ".jpeg" : "Images",
    ".tiff" : "Images",
    ".gif" : "Images",
    ".bmp" : "Images",
    ".svg" : "Images",
    

    # Videos
    ".mp4" : "Videos",
    ".wmv" : "Videos",
    ".avi" : "Videos",
    ".mov" : "Videos",
    ".wav" : "Videos",
    # Music
    ".mp3" : "Music",
    # Texts
    ".pdf" : "Texts",
    ".docx" : "Texts",
    ".doc" : "Texts",
    ".xls" : "Texts",
    ".xlx" : "Texts",
    ".xlsx" : "Texts",
    ".txt" : "Texts",
    
    # Executables
    ".exe" : "Executables",

    #Archives
    ".zip" : "Archives",
    ".7zip" : "Archives",
    ".rar" : "Archives",
    ".tar" : "Archives",


}

if not os.path.exists(f"./{sort_folder}"):
    print("created new directory")
    os.mkdir(sort_folder)

files = os.listdir(".")
for file in files:
    name, extension = os.path.splitext(file)
    if extension in filetypes:
        sort_in_folder(file, filetypes[extension])
    elif extension == "":
        continue
    elif name == "cleandirectory":
        continue
    else:
        sort_in_folder(file, "other")
         
    #for key in filetypes:



# get current directory

# get a list of all files in directory