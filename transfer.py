import settings
import os
import shutil


def transferFiles(directories):
    print("[ ] Beginning file transfer process")
    for file in os.scandir(settings.ROOT_DIR):
        subdirFound = False
        for dir, ext in directories:
            if file.name.endswith(ext):
                shutil.move(file.path, f"{dir}\\{file.name}")
                subdirFound = True
                break
        if not subdirFound:
            shutil.move(file.path, f"{settings.TARGET_DIR}\\{file.name}")
