import re
import os
import sys

def update_files(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' not found!")
        return

    # Patterns for identifying different URLs
    image_pattern = r"https://(?:images|ecs7)\.tokopedia\.net/([^\s]+\.(?:png|jpg))"
    file_pattern = r"https://assets\.tokopedia\.net/([^\s]+\.(?:csv|svg|pdf|xls|json|txt|xml|zip|mp4|webp))"

    # Function to update image URLs
    def replace_image_url(match):
        extracted_path = match.group(1)
        return f"https://p16-images-comn-sg.tokopedia-static.net/tos-alisg-i-zr7vqa5nfb-sg/{extracted_path}~tplv-zr7vqa5nfb-image.image"

    # Function to update file URLs (add prefix)
    def replace_file_url(match):
        extracted_path = match.group(1)
        return f"https://p16-assets-sg.tokopedia-static.net/tos-alisg-i-cqp9s0kcd0-sg/{extracted_path}"

    # Walk through all files in the folder and subfolders
    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Check if the file is a text-based file
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
            except (UnicodeDecodeError, IsADirectoryError):
                continue  # Skip binary files and directories

            # Replace image and file URLs
            updated_content = re.sub(image_pattern, replace_image_url, content)
            updated_content = re.sub(file_pattern, replace_file_url, updated_content)

            # Overwrite the file only if changes were made
            if content != updated_content:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(updated_content)
                print(f"✅ Updated: {file_path}")
            else:
                print(f"ℹ️ No changes: {file_path}")

# Get folder path from command-line argument or set manually
if len(sys.argv) > 1:
    folder_path = sys.argv[1]
else:
    folder_path = "/Users/bytedance/Documents/my_project"

# Run the function
update_files(folder_path)
