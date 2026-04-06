from config import load_categories
import hashlib

def get_file_hash(file_path):
    hasher = hashlib.md5()
    
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    
    return hasher.hexdigest()

FILE_CATEGORIES = load_categories()
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
