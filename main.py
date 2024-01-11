import tkinter as tk
from configparser import ConfigParser
from tkinter import ttk, filedialog
import os

import settings
from transfer import transferFiles


def __getSubdirectories():
    subdirectories = []
    for subdir in settings.TARGET_SUBDIRS:
        subdirectories.append(
            (os.path.join(settings.TARGET_DIR, subdir[0]), subdir[1]))
    # add target directory for moving all other file extensions
    # subdirectories.append((settings.TARGET_DIR, None))
    return subdirectories


def __createSubdirs(directories):
    for subdir in directories:
        try:
            if not os.path.lexists(subdir[0]):
                os.mkdir(subdir[0])
        except PermissionError as e:
            print(f"Subdirectory '{subdir[0]}' couldn't be created.")
            print(e)
        except:
            print(f"Subdirectory '{subdir[0]}' couldn't be created.")


def main():
    print("Would you like to use the GUI? (y/n): ")
    directories = __getSubdirectories()
    __createSubdirs(directories)
    # if user wants to use GUI, then run App instance
    # else run the program with default settings and parameters
    transferFiles(directories)


if __name__ == "__main__":
    main()

# app = App()
# app()
