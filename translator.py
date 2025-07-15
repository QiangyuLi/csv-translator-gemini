import pandas as pd
import google.generativeai as genai
from typing import List, Optional


class CSVTranslator:
    def __init__(self, api_key: str):
        """
        Initialize the Gemini translator with API key.
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def translate_batch(self, texts: List[str], target_lang: str) -> List[str]:
        """
        Translate a list of texts to the target language using Gemini.
        Returns a list of translated strings in the same order.
        """
        if not texts:
            return []

        # Construct a clear prompt
        prompt = f"""
You are a professional translator. Translate each bullet point below into {target_lang}.
Return only the translated list, preserving the order, using the same bullet format.
Do not include any explanations, extra punctuation, or numbering.

Example Input:
- Hello, how are you?
- I am fine, thank you.

Example Output (French):
- Bonjour, comment ça va ?
- Je vais bien, merci.

Now translate this list:
{chr(10).join([f"- {t}" for t in texts])}
"""

        try:
            response = self.model.generate_content(prompt.strip())
            lines = response.text.strip().split("\n")
            translations = [line.strip("- ").strip() for line in lines if line.strip()]

            if len(translations) != len(texts):
                print(f"⚠️ Translation mismatch: expected {len(texts)}, got {len(translations)}. Using original text.")
                return texts

            return translations
        except Exception as e:
            print(f"❌ Translation error: {e}")
            return texts

    def translate_csv_columns(
        self,
        df: pd.DataFrame,
        columns: List[str],
        target_lang: str,
        row_start: Optional[int] = 0,
        row_end: Optional[int] = None,
        batch_size: int = 10
    ) -> pd.DataFrame:
        """
        Translates selected columns in the DataFrame for the specified row range.
        Translation is done in batches for efficiency.
        """
        row_end = row_end or len(df)
        df_copy = df.copy()

        for col in columns:
            if col not in df.columns:
                print(f"⚠️ Column '{col}' not found. Skipping.")
                continue

            print(f"🔄 Translating column '{col}' to {target_lang}...")
            for i in range(row_start, row_end, batch_size):
                batch_indices = list(range(i, min(i + batch_size, row_end)))
                original_texts = df_copy.loc[batch_indices, col].astype(str).tolist()
                translated_texts = self.translate_batch(original_texts, target_lang)
                df_copy.loc[batch_indices, col] = translated_texts
                print(f"✅ Translated rows {i} to {i + len(translated_texts) - 1} in column '{col}'.")

        return df_copy
