# TXT to DOC Converter

A simple Python script that converts **one or more `.txt` files** into **Word `.docx` files**, saving each output file in the **same directory** as its input file.

The script **asks for input after it starts** (no command-line arguments required).

---

## Requirements

* Python **3.7 or newer**
* Internet access (one time, to install dependency)

---

## Setup Instructions

### 1. Verify Python is installed

Run:

```bash
python --version
```

If Python is not installed, download it from:

* [https://www.python.org/downloads/](https://www.python.org/downloads/)

> During installation on Windows, **check “Add Python to PATH”**.

---

### 2. Install required dependency

Run:

```bash
python -m pip install python-docx
```

✅ **Important**

* The package name is **`python-docx`**
* Do **NOT** install `docx` (that is a different, broken package)

If you accidentally installed it:

```bash
python -m pip uninstall docx
python -m pip install python-docx
```

---

### 3. Verify installation

Run:

```bash
python -c "import docx; print(docx.__version__)"
```

If this prints a version number, setup is complete.

---

## Script

Save the following file as **`txt_to_doc.py`**:

```python
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
```

---

## Usage Instructions

### 1. Run the script

```bash
python txt_to_doc.py
```

---

### 2. Enter input when prompted

Provide **one or more space-separated `.txt` file paths**.

#### Example:

```
/home/user/a.txt /home/user/b.txt "/home/user/files with space/c.txt"
```

---

### 3. Output

* Each `.txt` file is converted to `.docx`
* Output files are saved **in the same directory**
* Example:

  * `a.txt → a.docx`
  * `b.txt → b.docx`

---

## Notes & Behavior

* Supports **multiple files in one run**
* Supports **paths with spaces** (wrap them in quotes)
* Skips:

  * non-`.txt` files
  * missing files
* Output format is **`.docx`** (modern Microsoft Word format)

---

## Troubleshooting

### Error: `No module named 'docx'`

Run:

```bash
python -m pip install python-docx
```

Make sure the same `python` command is used for **both install and run**.

---
