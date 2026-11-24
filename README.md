
# EchoScribe 🎙️

EchoScribe is a meeting transcription and minutes generation application that converts audio recordings into text and extracts important meeting information.

## Features

- Upload audio recordings
- Convert speech into text using AssemblyAI
- Display the generated transcript
- Generate a short meeting summary
- Identify potential action items

## Technologies Used

- Python
- Flask
- HTML
- Tailwind CSS
- JavaScript
- AssemblyAI API

## Project Structure

```text
EchoScribe/
│
├── templates/
│   └── index.html
│
├── server.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Mithra72/EchoScribe.git
```

Navigate into the project:

```bash
cd EchoScribe
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file based on `.env.example` and add your own AssemblyAI API key.

## Run the Application

```bash
python server.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

1. Upload an audio file.
2. The Flask backend sends it for transcription using AssemblyAI.
3. The transcript is displayed on the webpage.
4. The application generates a basic summary using the first three sentences.
5. Potential action items are extracted using keyword matching.

## Future Improvements

- AI-powered meeting summarization
- Improved action item extraction
- Speaker identification
- Meeting report downloads

## Author

Mithra B
Nanthini R
