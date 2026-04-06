# Smart File Organizer

A Python-based automation tool that organizes files into categories and supports real-time monitoring.

## Features
- Organizes files by type (Images, Videos, Documents, etc.)
- Command Line Interface (CLI) with argparse
- Dry-run mode to preview actions
- Verbose logging for detailed output
- JSON-based configurable categories
- Duplicate file detection using hashing
- Real-time file monitoring using watchdog

## Tech Stack
- Python
- argparse
- logging
- watchdog

## Usage

```bash
python main.py <folder_path>
python main.py <folder_path> --dry-run
python main.py <folder_path> --verbose
python main.py <folder_path> --watch

file_organizer/
├── main.py
├── organizer.py
├── utils.py
├── config.py
├── watcher.py
├── logger.py
├── categories.json