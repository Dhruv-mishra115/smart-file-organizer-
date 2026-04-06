import argparse
from organizer import organize
#create parser first
parser = argparse.ArgumentParser(description="Smart File Organizer")

parser.add_argument("folder", help="Path of folder to organize")



parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Show what will happen without moving files"
)

parser.add_argument(
    "--verbose",
    action="store_true",
    help="Show detailed output"
)

parser.add_argument(
    "--watch",
    action="store_true",
    help="Watch folder and organize automatically"
)

args = parser.parse_args()
if args.watch:
    from watcher import start_watching
    start_watching(args.folder)
else:
    organize(args.folder, args.dry_run, args.verbose)