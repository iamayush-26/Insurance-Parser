import re
import pdfplumber
import json


PDF_PATH = r"C:\Users\ayush\Downloads\Assignment\pdf-health-insurance-policy_compress.pdf"



# ---------------------------------------------------------
# TEXT EXTRACTION
# ---------------------------------------------------------
def extract_text(pdf_path: str) -> str:
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


# ---------------------------------------------------------
# FIELD EXTRACTION
# ---------------------------------------------------------
def parse_fields(text: str) -> dict:
    data = {
        "policy_number": None,
        "name": None,
        "start_date": None,
        "end_date": None,
        "premium_paid": None,
        "sum_assured": None,
    }

    # Policy number
    m = re.search(r"Policy No\.?\s*[:\-]?\s*(P/[0-9/]+)", text)
    if m:
        data["policy_number"] = m.group(1)

    # Name (proposer)
    m = re.search(r"Proposer's Name\s*[:\-]?\s*([A-Z\s]+)", text)
    if m:
        data["name"] = m.group(1).strip()

    # Start & End dates
    m = re.search(r"FROM\s*[:\-]?\s*(\d{2}/\d{2}/\d{4}).*?TO\s*[:\-]?\s*.*?(\d{2}/\d{2}/\d{4})", text, re.S)
    if m:
        data["start_date"] = m.group(1)
        data["end_date"] = m.group(2)

    # Total premium
    m = re.search(r"Total Premium\s*:\s*Rs\.?\s*([0-9,\.]+)", text)
    if m:
        data["premium_paid"] = m.group(1).replace(",", "")

    # Sum insured
    m = re.search(r"LIMIT OF COVERAGE\s*:\s*Rs\.?\s*([0-9,]+)", text)
    if m:
        data["sum_assured"] = m.group(1).replace(",", "")

    return data


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    text = extract_text(PDF_PATH)
    data = parse_fields(text)

    print("\nEXTRACTED DATA:\n")
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()
