# Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.
import os
import shutil

src_file = "example.txt"
src_dir = "source_dir"
dst_dir = "target_dir"

os.makedirs(src_dir, exist_ok=True)
os.makedirs(dst_dir, exist_ok=True)

with open(os.path.join(src_dir, src_file), "w") as f:
    f.write("Sample content")

shutil.copy(os.path.join(src_dir, src_file), os.path.join(dst_dir, src_file))

print("File copied successfully.")
