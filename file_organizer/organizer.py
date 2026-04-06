from utils import get_extension, get_category
from utils import get_extension, get_category, get_file_hash
import os
import shutil
from logger import logger
from config import load_categories

FILE_CATEGORIES = load_categories()

seen_files = {}
def organize(folder_path, dry_run=False, verbose=False):

    if not os.path.exists(folder_path):
        print("ERROR: Folder does not exist!")
        return

    if not os.path.isdir(folder_path):
        print("ERROR: This is not a directory!")
        return

    for root, dirs, files in os.walk(folder_path):

        # prevent scanning category folders again
        dirs[:] = [d for d in dirs if d not in FILE_CATEGORIES]

        for file in files:

            full_path = os.path.join(root, file)

            file_hash = get_file_hash(full_path)

            if file_hash in seen_files:
                logger.info(f"Duplicate found: {file} (same as {seen_files[file_hash]})")
                continue
            else:
                seen_files[file_hash] = file

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

            if dry_run:
                logger.info(f"[DRY RUN] {file} would move to {category}")
            else:
                try:
                    shutil.move(full_path, destination)
                    logger.info(f"{file} moved to {category}")
                except Exception as e:
                    logger.error(f"Error moving {file}: {str(e)}")
                if verbose:
                    logger.info(f"{file} moved to {category}")

