import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

def extract_archive(filepaths, dest_dir):
    with zipfile.ZipFile(filepaths, 'r') as file:
       file.extractall(path=dest_dir)


if __name__ == "__main__":
    make_archive(filepaths=["ex.py", "be.py"], dest_dir="dest")
