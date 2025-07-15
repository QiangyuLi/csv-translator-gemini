# 📄 CSV Translator with Google Gemini API

Translate selected columns in a CSV file to any target language using the Google Gemini API via Python SDK.  
This tool is optimized for use in Google Colab, offering a simple and interactive environment.

---

## 🚀 Features

- Upload your CSV file directly in Colab
- Select specific columns to translate
- Choose your target language (e.g., "fr" for French, "zh" for Chinese)
- Automatically translates using Gemini (Google's generative AI model)
- Download the translated CSV for further use

---

## 🛠️ Requirements

- Python 3.8+
- Google Colab (preferred environment)
- Google Generative AI SDK (`google-generativeai`)
- `pandas`

---

## 📦 Installation

Inside your Colab notebook, install the required packages:

```python
!pip install -q google-generativeai pandas
````

---

## 🔐 API Key Setup

To use the Gemini API, you must configure your API key:

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
```

Get your API key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## 📝 Usage Instructions

1. Clone or upload the files to your Colab environment.
2. Run `main.ipynb`.
3. Upload your CSV file when prompted.
4. Specify:

   * Columns you want to translate
   * Target language (ISO language code)
5. Enter your Gemini API key.
6. Download the translated CSV.

---

## 📁 Repository Structure

```
csv-translator-gemini/
├── README.md
├── requirements.txt
├── translator.py         # Translation logic using Gemini
├── main.ipynb            # Google Colab notebook interface
```

---

## ⚠️ Disclaimer

This project uses the **Google Gemini API** to process and translate text content from CSV files.
Please note:

* This tool is for **educational and research purposes only**.
* You are solely responsible for complying with **Google's API Terms of Service** and any applicable data privacy laws when using this tool.
* Avoid uploading sensitive or personally identifiable information (PII) unless you are sure of compliance and data handling responsibilities.
* The translation output may not always be accurate; always review results before use in production settings.

---

## 📬 Contact

Feel free to open an issue or pull request if you’d like to contribute or report problems.

---

## 📝 License

MIT License

