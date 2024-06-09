import os
import shutil


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


folders = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".pl", ".rb"],
    "Other": []
}


for folder in folders:
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


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

print("Desktop has been organized")
