# Sign Language Translator

A web application that translates English text to Indian Sign Language (ISL) and provides video demonstrations for each word. It also generates similar sentences using AI.

## Features
- Translate English sentences to ISL (textual and video form)
- Generate similar sentences using GPT-2
- Example sentences for quick testing
- Modern, responsive UI/UX

## Setup Instructions

### 1. Clone the repository
```
git clone <repo-url>
cd Sign-Lang-Translater
```

### 2. (Optional) Create and activate a virtual environment
```
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the application
```
python app.py
```

The app will be available at http://localhost:5100

## Usage
- Enter your sentence in the input box.
- (Optional) Click on an example sentence to auto-fill the input.
- Click "Process Text" to see the ISL translation and matched videos.
- If "Generate sentences" is checked, you will also see AI-generated similar sentences.

## Project Structure
- `app.py` - Main Flask application
- `translator.py` - Text processing and ISL translation logic
- `generated_text.py` - AI-based sentence generation
- `static/` - CSS, JS, and video files
- `templates/` - HTML templates

## Notes
- The ISL video matching works for words that have a corresponding video in `static/videos/`.
- English-to-Hindi translation is currently disabled due to unavailable dependencies.

---
Feel free to contribute or suggest improvements! 