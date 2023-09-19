# Sentiment Analysis API with Flask and NLTK

This is a simple Flask application that provides endpoints for sentiment analysis using the VADER sentiment analysis library from NLTK.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
    - [Analyzing Sentiment for an Array of Articles](#analyzing-sentiment-for-an-array-of-articles)
    - [Analyzing Sentiment for a Single Text](#analyzing-sentiment-for-a-single-text)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. Navigate to the project directory
    ```bash
    cd yourrepository
    ```

3. Create a virtual environment
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the Flask application
```bash
flask run
```

### Analyzing Sentiment for an Array of Articles

- **URL**: `/analyze_sentiment_arr`
- **Method**: `POST`
- **Data Example**: 
    ```json
    [
        {
            "title": "This is title 1",
            "description": "Description 1"
        },
        {
            "title": "This is title 2",
            "description": "Description 2"
        }
    ]
    ```

### Analyzing Sentiment for a Single Text

- **URL**: `/analyze_sentiment_single`
- **Method**: `POST`
- **Data Example**: 
    ```json
    {
        "text": "This is a sample text."
    }
    ```

## Contributing

If you would like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

MIT License. See the [LICENSE](LICENSE) file for details.

---

This README file should help people understand what your project is about, how to set it up, and how to use it. Feel free to expand on any sections as needed!
