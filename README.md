# CSV Translator with Google Gemini

Translate selected columns in a CSV file using the Google Gemini API (via Python SDK). Designed for Colab usage.

## Features
- Upload CSV file
- Choose columns to translate
- Set target language (e.g. "fr", "zh", "es")
- Uses Gemini API to translate via Google AI SDK

## Requirements
- Python 3.8+
- Google AI Python SDK
- Google Colab (for GUI interface)

## Setup (in Colab)

1. Install requirements:
```python
!pip install -q google-generativeai pandas
