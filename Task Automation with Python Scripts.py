import os
import shutil

def move_jpg_files(source_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for file in os.listdir(source_folder):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(source_folder, file),
                        os.path.join(target_folder, file))
            print(f"Moved: {file}")

# Example usage
move_jpg_files("source_folder", "jpg_images")
