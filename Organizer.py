import os
import shutil
import sys


FILE_CATEGORIES = {
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Videos": ["mp4", "mkv", "avi"],
    "Documents": ["pdf", "docx", "txt"],
    "Audio": ["mp3", "wav"],
    "Code": ["py", "js", "html", "css"]
}


def get_extension(file_name):
    if "." in file_name:
        return file_name.split(".")[-1].lower()
    return None


def get_category(extension):
    if extension is None:
        return "Others"

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize(folder_path):

    for root, dirs, files in os.walk(folder_path):

        # prevent scanning category folders again
        dirs[:] = [d for d in dirs if d not in FILE_CATEGORIES]

        for file in files:

            full_path = os.path.join(root, file)

            extension = get_extension(file)

            category = get_category(extension)

            category_folder = os.path.join(folder_path, category)

            os.makedirs(category_folder, exist_ok=True)

            destination = os.path.join(category_folder, file)

            # duplicate protection
            counter = 1
            while os.path.exists(destination):
                name, ext = os.path.splitext(file)
                new_name = f"{name}({counter}){ext}"
                destination = os.path.join(category_folder, new_name)
                counter += 1

            shutil.move(full_path, destination)

            print(f"{file} → moved to {category}")


if len(sys.argv) < 2:
    print("Usage: python organizer.py <folder_path>")
    sys.exit()

folder_path = sys.argv[1]

organize(folder_path)