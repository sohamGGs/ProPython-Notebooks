import os
import shutil

def organize_folder(target_dir: str):
    for filename in os.listdir(target_dir):
        if os.path.isfile(filename) and "." in filename:
            ext = filename.split(".")[-1]
            folder_name = f"{ext.upper()}_Files"
            
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            
            shutil.move(filename, f"{folder_name}/{filename}")
            print(f"Moved {filename} to {folder_name}")

if __name__ == "__main__":
    # Create some dummy files to organize
    open("test1.txt", "a").close()
    open("data.csv", "a").close()
    open("script.py", "a").close()
    
    organize_folder(".")