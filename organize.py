import os
import shutil

# Define the path to your desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define the folders and the file extensions that belong to each folder
folders = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".pl", ".rb"],
    "Other": []
}

# Create folders on the desktop if they do not exist
for folder in folders:
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to their respective folders
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)
    if os.path.isfile(item_path):
        moved = False
        for folder, extensions in folders.items():
            if item.lower().endswith(tuple(extensions)):
                shutil.move(item_path, os.path.join(desktop_path, folder, item))
                moved = True
                break
        if not moved:
            shutil.move(item_path, os.path.join(desktop_path, "Other", item))

print("Desktop has been orgainzed")
