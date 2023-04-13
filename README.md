<pre>
# Facebook Post Generator

This project generates multiple creative and engaging variations of Facebook posts based on a given input text. The primary goal is to provide users with different options for their social media content, allowing them to choose the one that best suits their needs.

## Features

- Takes an input text file containing the content to be used for generating Facebook posts
- Generates a specified number of variations for each post
- Saves each variation in a separate text file within the 'summaries' folder

## Getting Started

### Prerequisites

- Python 3.x
- An OpenAI API key (get one by signing up at https://beta.openai.com/signup/)

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/facebook-post-generator.git
```

2. Change into the project directory:

```
cd facebook-post-generator
```

3. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Create a file named `key_openai.txt` in the project directory and paste your OpenAI API key inside it.

### Usage

1. Add the content you'd like to generate Facebook posts from to the `input.txt` file.

2. Run the script:

```
python post_generator.py
```

3. The generated variations will be saved in separate text files within the 'summaries' folder.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
</pre>
