# file extensions
DOCUMENTS = ("pdf", "docx", "zip", "doc", "odt", "txt")
EXECUTABLES = ("exe", "bat", "com", "cmd",
               "inf", "ipa", "osx", "pif", "run", "wsh")
IMAGES = ("jpg", "jpeg", "gif", "psd", "eps", "png", "webp",
          "tiff", "svg", "raw", "bmp", "xcf", "ico", "jfif")
OTHER = ("msi", "ics", "html", "zip", "7z")
SCRIPTS = ("py", "js", "jsx", "tsx")
VIDEOS = ("avi", "mp4", "webm", "flv", "mkv", "mov", "wmv", "ogg", "mpeg")

# directories
ROOT_DIR = "D:\\testdir\\root"
TARGET_DIR = "D:\\testdir\\target"

TARGET_SUBDIRS = [
    ("Documents", DOCUMENTS),
    ("Executables", EXECUTABLES),
    ("Other", OTHER),
    ("Pictures", IMAGES),
    ("Scripts", SCRIPTS),
    ("Videos", VIDEOS),
]
