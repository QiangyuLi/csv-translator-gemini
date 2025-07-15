# 📄 CSV Translator with Google Gemini API (Command-Line Ready)

This tool allows you to **translate selected columns in a CSV file** using the **Google Gemini API** via Python.  
It supports **batch translation**, **row filtering**, and is fully runnable via **command-line in Google Colab or local environments**.

---

## 🚀 Features

- 🔍 Translate only specific columns (e.g. "title", "description")
- 🌍 Choose any target language (e.g. `"fr"` for French, `"zh"` for Chinese)
- 📊 Translate selected rows (row range) in batches
- ✅ Uses Gemini (`gemini-pro`) via `google-generativeai` SDK
- 💻 Command-line interface ready (e.g., run `main.py` with flags)

---

## 📦 Installation

In Colab or your Python environment:

```bash
pip install google-generativeai pandas
````

---

## 📁 Project Structure

```
csv-translator-gemini/
├── main.py               # Main script to run from CLI
├── translator.py         # Translation logic using Gemini
├── requirements.txt
└── README.md
```

---

## 🔧 Usage (Command-Line in Colab or Terminal)

```bash
python3 main.py \
  --api_key="YOUR_GEMINI_API_KEY" \
  --input="sample.csv" \
  --output="translated_sample.csv" \
  --columns="title,description" \
  --language="fr" \
  --row_start=0 \
  --row_end=50 \
  --batch_size=10
```

### 🔑 Arguments

| Flag           | Description                                     |
| -------------- | ----------------------------------------------- |
| `--api_key`    | Your Gemini API key                             |
| `--input`      | Path to input CSV file                          |
| `--output`     | Path to save the translated CSV                 |
| `--columns`    | Comma-separated list of columns to translate    |
| `--language`   | Target language code (e.g. `es`, `zh`, `fr`)    |
| `--row_start`  | (Optional) Start row index (default: 0)         |
| `--row_end`    | (Optional) End row index (default: full length) |
| `--batch_size` | (Optional) Number of rows to translate at once  |

---

## 🧠 Gemini Prompt Design

This tool uses a carefully constructed prompt to Gemini for accurate batch translation.
It ensures outputs are clean, ordered, and aligned with input rows using bullet formatting.

---

## ⚠️ Disclaimer

This project is for **educational and research use only**.

* You are responsible for complying with **Google's API terms** and **data protection laws**.
* Do **not upload sensitive or personal data** unless fully anonymized and authorized.
* Translation quality may vary; always review outputs before use in production workflows.

---

## 📄 License

MIT License

---

## 🙋 Need Help?

Open an issue or contact the project maintainer for support.

