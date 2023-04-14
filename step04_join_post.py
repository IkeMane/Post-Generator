import os
def main():
    # Define the path to the directory containing the text files
    folder_path = "post"

    # Create a list to store the contents of each file
    file_contents = []

    # Loop through each file in the directory
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            # Open the file and read its contents as UTF-8, ignoring errors
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8", errors="ignore") as f:
                file_contents.append(f.read())

    # Merge the contents of all files with a double newline between each chunk
    merged_contents = "\n\n".join(file_contents)

    # Write the merged contents to a new file called "all_post.txt" as UTF-8, ignoring errors
    with open("all_post.txt", "w", encoding="utf-8", errors="ignore") as f:
        f.write(merged_contents)