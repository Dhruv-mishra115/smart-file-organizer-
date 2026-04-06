import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
from organizer import organize
from utils import get_extension, get_category
import shutil


class WatchHandler(FileSystemEventHandler):
    def __init__(self, folder):
        self.folder = folder

    def on_created(self, event):
        if event.is_directory:
            return

        # ❌ Ignore files already inside category folders
        if any(folder in event.src_path for folder in ["Images", "Videos", "Documents", "Audio", "Code"]):
            return

        print(f"New file detected: {event.src_path}")

        # wait for file to stabilize
        for _ in range(5):
            try:
                size1 = os.path.getsize(event.src_path)
                time.sleep(0.5)
                size2 = os.path.getsize(event.src_path)
                if size1 == size2:
                    break
            except:
                time.sleep(0.5)

        file = os.path.basename(event.src_path)
        extension = get_extension(file)
        category = get_category(extension)

        destination_folder = os.path.join(self.folder, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination = os.path.join(destination_folder, file)

        try:
            shutil.move(event.src_path, destination)
            print(f"{file} moved to {category}")
        except Exception as e:
            print(f"Error moving file: {e}")


def start_watching(folder_path):
    event_handler = WatchHandler(folder_path)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)

    observer.start()
    print(f"Watching folder: {folder_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()