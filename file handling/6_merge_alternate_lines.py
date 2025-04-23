# Write a program that merges lines alternatively from two files and writes the results to new file.
file1 = "file1.txt"
file2 = "file2.txt"
outfile = "merged.txt"

with open(file1, "w") as f:
    f.write("Line1 from file1\nLine2 from file1\nLine3 from file1\n")

with open(file2, "w") as f:
    f.write("Line1 from file2\nLine2 from file2\n")

with open(file1, "r") as f1, open(file2, "r") as f2, open(outfile, "w") as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])

print("Files merged alternatively.")
