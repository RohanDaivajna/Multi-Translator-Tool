# Translator Application

This project is a graphical user interface (GUI) application for language translation and Morse code conversion. It uses the `googletrans` library for translation and a custom implementation for Morse code translation.

## Project Structure

- `Translator.py` - The main Python script for the application.
- `translation.ico` - The icon file used in the application.
- `requirements.txt` - Lists the required Python packages.
- `Translator.exe` - The compiled executable file.

## Features

- **Language Translator**: Translate text between different languages using Google Translate.
- **Morse Code Translator**: Convert text to and from Morse code.
- **Morse Code Lookup**: View a visual representation of Morse code.

## Installation

### Prerequisites

- Python 3.6 or later
- `pip` (Python package installer)

### Setup

1. **Clone the Repository**
   git clone https://github.com/yourusername/yourrepository.git
   
   cd yourrepository

3. **Create and Activate a Virtual Environment**
    python -m venv env

    On Windows:
    env\Scripts\activate

    On macOS/Linux:
    source env/bin/activate

4. **Install Required Packages**
    pip install -r requirements.txt

5. **Running the Application**
    To run the application directly from the Python script:
    python Translator.py



#To run the compiled executable:

1.**Navigate to the Directory Containing Translator.exe**
    cd yourdirectory

When running Translator.exe, make sure that the translation.ico file is in the same directory as the executable. The application requires this file for its icon.

2.**Run the Executable**
    Translator.exe
