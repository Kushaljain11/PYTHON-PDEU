# Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.
src_file = "source.txt"
dst_file = "destination.txt"

with open(src_file, "w") as f:
    f.write("This is a Sample text with lowercase letters.")

with open(src_file, "r") as f_src:
    content = f_src.read().upper()

with open(dst_file, "w") as f_dst:
    f_dst.write(content)

print("Content copied with uppercase transformation.")
