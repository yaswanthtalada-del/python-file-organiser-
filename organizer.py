import os
import shutil

folder_path = "C:/Users/Downloads"

extensions = {
    'Images': ['.jpg', '.png', '.jpeg'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv']
}

for filename in os.listdir(folder_path):
    for folder, exts in extensions.items():
        if filename.endswith(tuple(exts)):
            folder_dir = os.path.join(folder_path, folder)
            if not os.path.exists(folder_dir):
                os.mkdir(folder_dir)
            shutil.move(os.path.join(folder_path, filename), os.path.join(folder_dir, filename))
            print(f"Moved {filename} to {folder}")

print("File organization complete!")