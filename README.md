# Sentiment Analysis API with FastAPI and NLTK

This is a FastAPI application that provides endpoints for sentiment analysis using the VADER sentiment analysis library from NLTK. It is containerized using Docker and uses Taskfile.dev for automating tasks.

## Table of Contents
- [Installation](#installation)
- [Docker Setup](#docker-setup)
- [Usage](#usage)
    - [Analyzing Sentiment for an Array of Articles](#analyzing-sentiment-for-an-array-of-articles)
    - [Analyzing Sentiment for a Single Text](#analyzing-sentiment-for-a-single-text)
- [Task Automation with Taskfile.dev](#task-automation-with-taskfiledev)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/pauloberezini/sentiment-analysis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd sentiment-analysis
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate     # On Windows
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Docker Setup

Ensure Docker is installed on your machine.

1. Build the Docker image:
    ```bash
    docker build -t sentiment:tag .
    ```

2. Run the Docker container:
    ```bash
    docker run --name sentiment --hostname sentiment.com --network my-net -d -e TZ=Asia/Jerusalem --restart unless-stopped -p 5051:8000 sentiment:tag
    ```

## Usage

Run the FastAPI application:
```bash
uvicorn main:app --reload
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
        "description": "This is a sample text."
    }
    ```

## Task Automation with Taskfile.dev

For convenience, tasks like building, running, and removing the Docker container are automated using Taskfile.dev. You can find the task definitions in the provided `taskfile.yml`.

Example commands:

- Build the Docker image:
    ```bash
    task build
    ```

- Run the Docker container:
    ```bash
    task run
    ```

- Remove the Docker container:
    ```bash
    task rm
    ```

- Remove the Docker image:
    ```bash
    task rmall
    ```

## Contributing

If you would like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

MIT License. See the [LICENSE](LICENSE) file for details.

---

Your repository link is now embedded in the README. If there are any other modifications you'd like, let me know!
