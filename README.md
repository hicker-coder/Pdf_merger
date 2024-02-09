# PDF Merger

## Introduction
PDF Merger is a Python script designed to merge multiple PDF files within a specified folder into a single PDF file. This script utilizes the PyPDF2 library for PDF manipulation and offers a convenient way to combine PDF documents.

## Features
- Merges all PDF files within a specified folder into one PDF file.
- Sorts PDF files based on their last modified time before merging.
- Provides error handling for cases such as folder not found or other unexpected errors.
- Written in compliance with PEP 8 style guidelines.
- Utilizes classes, decorators, and type hints for better code organization and readability.

## Usage
1. Clone or download the script to your local machine.
2. Ensure you have Python installed on your system along with the PyPDF2 library. You can install PyPDF2 via pip:

    ```
    pip install PyPDF2
    ```

3. Place all the PDF files you want to merge into a folder.
4. Open the script `pdf_merger.py` and set the `folder_path` variable to the path of the folder containing the PDF files.
5. Specify the desired output path for the merged PDF file by setting the `output_path` variable.
6. Run the script by executing the following command in your terminal:

    ```
    python pdf_merger.py
    ```

7. The merged PDF file will be created at the specified output path.

## Error Handling
- If the specified folder path does not exist, the script will raise a `FileNotFoundError`.
- If any unexpected error occurs during the merging process, it will be caught and displayed, ensuring graceful handling of errors.

## Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This script is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
