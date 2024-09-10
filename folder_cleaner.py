import sys
from pathlib import Path


CATEGORIES = {"Music": [".mp3", ".wav", ".flac", ".wma"],
              "Docs": [".docs", ".pdf", ".txt"],
              "Pictures": ['.JPEG', '.PNG', '.JPG', '.SVG'],
              "Video": ['.AVI', '.MP4', '.MOV', '.MKV'],
              "Archive": [".zip", '.gz', '.tar']
              }


def get_categories(file: Path):
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def move_file(file: Path, category: str, root_dir: Path):
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    file.replace(target_dir.joinpath(file.name))


def sort_folder(path: Path):

    for item in path.glob("**/*"):
        folders = [f for f in path.glob("**/") if f.is_dir()]
        if item.is_file():
            category = get_categories(item)
            move_file(item, category, path)

    for folder in folders[::-1]:
        try:
            folder.rmdir()
        except OSError:
            pass


def main():

    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
    if not path.exists():
        return "Folder doesn't exist"
    sort_folder(path) 


if __name__ == '__main__':
    main()
