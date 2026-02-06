# Insurance Policy Parser

This project implements a Python-based parser that extracts key financial
and policy-related fields from a health insurance PDF document.

## Extracted Fields
- Policy Number
- Policy Holder Name
- Policy Start Date
- Policy End Date
- Premium Paid
- Sum Assured

## Approach
The parser uses:
- **pdfplumber** for direct PDF text extraction
- **Regular Expressions (Regex)** for structured field detection

<img width="921" height="359" alt="Screenshot 2026-02-06 210612" src="https://github.com/user-attachments/assets/ad848b00-0357-4892-bca5-cae46c2ff095" />

This approach was chosen because:
- Insurance documents follow semi-structured layouts
- Regex enables accurate and fast extraction
- No heavy ML model is required for clean PDFs

## How to Run

```bash
pip install pdfplumber
python health_policy_parser.py
