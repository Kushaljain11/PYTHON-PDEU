# Given a text file, write a program to create another text file deleting 'a', 'the', 'an' and replacing each one with a blank space.
input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "w") as f:
    f.write("This is a text with the, a, and an articles to remove.")

with open(input_file, "r") as f:
    text = f.read()

for word in [" a ", " an ", " the "]:
    text = text.replace(word, " ")

with open(output_file, "w") as f:
    f.write(text)

print("Articles removed and new file created.")
