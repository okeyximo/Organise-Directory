#!/bin/bash

download_dir="/Users/okeyx/Downloads"
target_dir="/Users/okeyx/myfiles/organised"

# Define file extensions and corresponding target directories
pdf_extensions=("pdf")
text_extensions=("txt")
image_extensions=("jpg" "png")
document_extensions=("docx")
video_extensions=("mp4" "mov")
music_extensions=("mp3" "flac")

# Function to determine target directory based on file extension
get_target_directory() {
    local file_extension=$1
    if [[ " ${pdf_extensions[@]} " =~ " $file_extension " ]]; then
        echo "$target_dir/pdf"
    elif [[ " ${text_extensions[@]} " =~ " $file_extension " ]]; then
        echo "$target_dir/text"
    elif [[ " ${image_extensions[@]} " =~ " $file_extension " ]]; then
        echo "$target_dir/images"
    elif [[ " ${document_extensions[@]} " =~ " $file_extension " ]]; then
        echo "$target_dir/documents"
    elif [[ " ${video_extensions[@]} " =~ " $file_extension " ]]; then
        echo "$target_dir/videos"
    elif [[ " ${music_extensions[@]} " =~ " $file_extension " ]]; then
        echo "$target_dir/music"
    else
        echo "$target_dir/other"
    fi
}

# Loop through files in the download directory
for file in "$download_dir"/*; do
    if [ -f "$file" ]; then
        file_extension="${file##*.}"
        file_extension=$(echo "$file_extension" | tr '[:upper:]' '[:lower:]')  # Convert to lowercase
        target_subdir=$(get_target_directory "$file_extension")

        # Create target subdirectory if it doesn't exist
        mkdir -p "$target_subdir"

        # Move the file to the target subdirectory
        mv "$file" "$target_subdir"
    fi
done
