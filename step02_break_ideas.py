import os

def main(input_file):
    # Read the content from the input file
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Split the content into chunks based on a delimiter (e.g., double newline)
    chunks = content.split("\n\n")

    # Ensure the 'summaries' directory exists
    summaries_dir = "post_ideas"
    if not os.path.exists(summaries_dir):
        os.makedirs(summaries_dir)

    # Create a new text file for each chunk in the 'summaries' folder
    for i, chunk in enumerate(chunks):
        with open(os.path.join(summaries_dir, f"chunk_{i + 1}.txt"), "w", encoding="utf-8", errors="ignore") as f:
            f.write(chunk)

def main1():
    input_file = "post_ideas/post_ideas.txt"
    main(input_file)
