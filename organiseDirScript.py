import os
import shutil

def organize_downloads(download_dir, target_dir):
    # Dictionary mapping file extensions to their corresponding subdirectories
    file_extensions = {
        "pdf": "pdf",
        "txt": "text",
        "jpg": "images",
        "png": "images",
        "docx": "documents",
        # Add more extensions as needed
    }

    # List all files in the download directory
    files = os.listdir(download_dir)

    for file in files:
        if os.path.isfile(os.path.join(download_dir, file)):
            file_extension = os.path.splitext(file)[1][1:].lower()
            target_subdir = os.path.join(target_dir, file_extensions.get(file_extension, "other"))

            # Create the target subdirectory if it doesn't exist
            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)

            # Move the file to the target subdirectory
            shutil.move(os.path.join(download_dir, file), os.path.join(target_subdir, file))

def main():
    # Replace these paths with your actual download directory and target directory
    download_directory = "/Users/okeyx/Downloads"
    target_directory = "/Users/okeyx/Downloads/organised"

    organize_downloads(download_directory, target_directory)

if __name__ == "__main__":
    main()