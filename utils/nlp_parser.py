import re

def extract_key_info(text):
    """
    Uses Regex to extract Invoice Number, Date, and Amount from raw text.
    """
    data = {
        "invoice_number": None,
        "date": None,
        "total_amount": None,
        "raw_text": text.strip()
    }

    # Regex patterns (Adjust based on document type)
    # Looking for patterns like "Invoice #12345"
    inv_match = re.search(r'(?i)invoice\s*[:#]?\s*([A-Za-z0-9-]+)', text)
    if inv_match:
        data["invoice_number"] = inv_match.group(1)

    # Looking for dates (e.g., 20-10-2023 or 20/10/2023)
    date_match = re.search(r'(\d{2}[-/\.]\d{2}[-/\.]\d{4})', text)
    if date_match:
        data["date"] = date_match.group(1)

    # Looking for currency/amounts
    amount_match = re.search(r'Total\s*[:]?\s*[$₹]?\s*(\d+[.,]\d{2})', text, re.IGNORECASE)
    if amount_match:
        data["total_amount"] = amount_match.group(1)

    return data