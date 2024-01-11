import os
import settings
from transfer import transferFiles


def __getSubdirectories():
    subdirectories = []
    for subdir in settings.TARGET_SUBDIRS:
        subdirectories.append(
            (os.path.join(settings.TARGET_DIR, subdir[0]), subdir[1]))
    return subdirectories


def __createSubdirs(directories):
    print("[ ] Verifying subdirectories' existences...")
    for subdir in directories:
        try:
            if not os.path.lexists(subdir[0]):
                print(f"[ ] Making directory for '{subdir[0]}'")
                os.mkdir(subdir[0])
        except PermissionError as e:
            print(f"Subdirectory '{subdir[0]}' couldn't be created.")
            print(e)
        except:
            print(f"Subdirectory '{subdir[0]}' couldn't be created.")


def main():
    print(
        f"[ ] Files are being moved from {settings.ROOT_DIR} to {settings.TARGET_DIR}")
    directories = __getSubdirectories()
    __createSubdirs(directories)
    transferFiles(directories)
    print("[✓] Process has completed without issue")


if __name__ == "__main__":
    main()
