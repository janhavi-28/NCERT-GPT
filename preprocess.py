# preprocess.py
import fitz
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    input_pdf = "data/class9_science.pdf"            # ← updated
    output_txt = "docs/class9_science.txt"           # ← updated

    if not os.path.exists(input_pdf):
        print(f"❌ File not found: {input_pdf}")
        print("📁 Please place the PDF inside the 'data/' folder with the correct name.")
        exit()

    os.makedirs("docs", exist_ok=True)

    text = extract_text_from_pdf(input_pdf)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Extracted text saved to: {output_txt}")
