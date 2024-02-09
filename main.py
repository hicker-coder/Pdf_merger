import os
from typing import List
from PyPDF2 import PdfMerger


class PDFMerger:
    def __init__(self, folder_path: str, output_path: str):
        self.folder_path = folder_path
        self.output_path = output_path

    def merge_pdfs_in_folder(self):
        pdf_files = self._get_pdf_files()
        merger = PdfMerger()

        for pdf_file in pdf_files:
            with open(os.path.join(self.folder_path, pdf_file), 'rb') as file:
                merger.append(file)

        with open(self.output_path, 'wb') as output_file:
            merger.write(output_file)

    def _get_pdf_files(self) -> List[str]:
        try:
            pdf_files = sorted([f for f in os.listdir(self.folder_path) if f.endswith('.pdf')],
                               key=lambda f: os.path.getmtime(os.path.join(self.folder_path, f)))
            return pdf_files
        except FileNotFoundError:
            raise FileNotFoundError(f"Folder not found: {self.folder_path}")

    @staticmethod
    def handle_errors(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        return wrapper


@PDFMerger.handle_errors
def main():
    # Set folder path to the current directory
    folder_path = os.getcwd()

    # Example output path
    output_path = 'merged_output.pdf'

    merger = PDFMerger(folder_path, output_path)
    merger.merge_pdfs_in_folder()


if __name__ == "__main__":
    main()
