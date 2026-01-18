import os
from docx import Document

def convert_txt_to_doc(txt_path):
    txt_path = txt_path.strip().strip('"')

    if not txt_path.lower().endswith(".txt"):
        print(f"Skipping (not a .txt file): {txt_path}")
        return

    if not os.path.isfile(txt_path):
        print(f"File not found: {txt_path}")
        return

    doc = Document()

    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            doc.add_paragraph(line.rstrip())

    output_path = os.path.splitext(txt_path)[0] + ".docx"
    doc.save(output_path)

    print(f"Converted: {output_path}")

def main():
    input_str = input(
        "Enter one or more space-separated .txt file paths:\n"
    ).strip()

    if not input_str:
        print("No input provided.")
        return

    txt_files = input_str.split()

    for txt_file in txt_files:
        convert_txt_to_doc(txt_file)

if __name__ == "__main__":
    main()
