# File Organizer Script

This Bash script is designed to organize files in a specified directory based on their file types (extensions). It categorizes files into different directories such as PDFs, text files, images, documents, videos, music, and others.

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/okeyximo/organise-directory.git
   ```

2. **Navigate to the Script Directory**:

   ```bash
   cd organise-Directory
   ```

3. **Edit the Script (Optional)**:

   - Open `organize.sh` in a text editor.
   - Modify `download_dir` and `target_dir` variables to specify your download directory and the target directory where files will be organized.

4. **Make the Script Executable**:

   ```bash
   chmod +x organize.sh
   ```

5. **Run the Script**:

   ```bash
   ./organize.sh
   ```

6. **Verify the Results**:
   - Check the specified target directory to ensure that files have been organized according to their types.

## Customization

You can customize the script by modifying the following variables in `organize.sh`:

- `download_dir`: The directory where your downloaded files are located.
- `target_dir`: The directory where organized files will be moved.
- Customize file extensions and corresponding directories in the script based on your requirements.

## Scheduled Execution

You can schedule the script to run periodically using `crontab`:

1. Open `crontab` for editing:

   ```bash
   crontab -e
   ```

2. Add the following line to run the script twice a day (e.g., at 9:00 AM and 9:00 PM):

   ```bash
   0 9,21 * * * /path/to/organize.sh
   ```

   Replace `/path/to/organize.sh` with the actual path to your `organize.sh` script.

3. Save and exit the editor.

## Notes

- This script categorizes files based on their file extensions and moves them to corresponding directories.
- Ensure that the target directory exists and that the script has appropriate permissions to write to it.
