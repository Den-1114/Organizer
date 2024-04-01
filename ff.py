import os
import shutil
import sys

# Define the file categories
file_categories = {
    ".html": "Cite",
    ".css": "Cite",
    ".js": "JavaScript",
    ".php": "PHP",
    ".c": "C",
    ".cpp": "C++",
    ".java": "java",
    ".sql": "database",
    ".xml": "xml",
    ".json": "json",
    ".md": "markdown",
    ".txt": "text",
    ".log": "log",
    ".pdf": "pdf",
    ".doc": "documents",
    ".docx": "documents",
    ".odt": "odt",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".xls": "Excel",
    ".xlsx": "Excel",
    ".rtf": "Rich Text Format",
    ".csv": "CSV",
    ".bmp": "bmp",
    ".gif": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".svg": "Scable Vector Graphics",
    ".avi": "Videos",
    ".mov": "Videos",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".wma": "Music",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".gifv": "Videos",
    ".iso": "Images",
    ".rar": "Archives",
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".7z": "Archives",
    ".bz2": "Archives",
    ".deb": "Archives",
    ".rpm": "Archives",
    ".pkg": "Archives",
    ".dmg": "Archives",
    ".iso": "Archives",
    ".vhd": "Archives",
    ".vhdx": "Archives",
    ".vdi": "Archives",
    ".iso": "Archives",
    ".bin": "Archives",
    ".msi": "Archives",
    ".cab": "Archives",
    ".apk": "Android Apps",
    ".deb": "Debian",
    ".rpm": "Red Hat",
    ".dmg": "MacOS",
    ".iso": "ISO",
    ".exe": "Apps",
    ".py": "Python",
}

# Path to the directory
directory = sys.path[0]

# Loop through all the files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    # Check if the file is a regular file
    if os.path.isfile(filepath):
        # Get the file extension
        extension = os.path.splitext(filename)[1]

        # Check if the file extension is present in the file categories
        if extension in file_categories:
            # Get the category for the file extension
            category = file_categories[extension]

            # Check if a directory exists for the category
            if not os.path.exists(category):
                # Create a directory for the category
                os.mkdir(category)

            # Move the file to the corresponding category directory
            shutil.move(filepath, os.path.join(category, filename))

print("File organization completed!")