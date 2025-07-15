import argparse
import pandas as pd
from translator import CSVTranslator

def parse_args():
    parser = argparse.ArgumentParser(description="Translate selected columns in a CSV using Gemini API")
    parser.add_argument('--api_key', required=True, help='Your Google Gemini API key')
    parser.add_argument('--input', required=True, help='Input CSV file path')
    parser.add_argument('--output', required=True, help='Output CSV file path')
    parser.add_argument('--columns', required=True, help='Comma-separated column names to translate')
    parser.add_argument('--language', required=True, help='Target language (e.g., "fr", "es", "zh")')
    parser.add_argument('--row_start', type=int, default=0, help='Start row index (default: 0)')
    parser.add_argument('--row_end', type=int, default=None, help='End row index (default: full length)')
    parser.add_argument('--batch_size', type=int, default=10, help='Batch size for translation (default: 10)')
    return parser.parse_args()

def main():
    args = parse_args()

    df = pd.read_csv(args.input)
    columns = [col.strip() for col in args.columns.split(",")]

    translator = CSVTranslator(api_key=args.api_key)
    translated_df = translator.translate_csv_columns(
        df,
        columns=columns,
        target_lang=args.language,
        row_start=args.row_start,
        row_end=args.row_end,
        batch_size=args.batch_size
    )

    translated_df.to_csv(args.output, index=False)
    print(f"Translated CSV saved to: {args.output}")

if __name__ == "__main__":
    main()
