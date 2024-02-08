import os
import shutil

def organize_downloads(download_dir, target_dir):
    file_extensions = {
        "pdf": "pdf",
        "txt": "text",
        "jpg": "images",
        "png": "images",
        "docx": "documents"
    }

    files = os.listdir(download_dir)

    for file in files:
        if os.path.isfile(os.path.join(download_dir, file)):
            file_extension = os.path.splitext(file)[1][1:].lower()
            target_subdir = os.path.join(target_dir, file_extensions.get(file_extension, "other"))

            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)

            shutil.move(os.path.join(download_dir, file), os.path.join(target_subdir, file))

def main():
    download_directory = "/Users/okeyx/Downloads"
    target_directory = "/Users/okeyx/myfiles/organised"

    organize_downloads(download_directory, target_directory)

if __name__ == "__main__":
    main()