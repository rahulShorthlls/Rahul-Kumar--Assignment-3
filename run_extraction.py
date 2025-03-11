# filepath: c:\Users\poora\OneDrive\Desktop\Assignment-1\run_extraction.py
from file_loader import PDFLoader, DOCXLoader, PPTLoader
from data_extractor import PDFDataExtractor, DOCXDataExtractor, PPTDataExtractor
from storage import FileStorage, SQLStorage

def main():
    pdf_loader = PDFLoader()
    docx_loader = DOCXLoader()
    ppt_loader = PPTLoader()

    pdf_extractor = PDFDataExtractor(pdf_loader)
    docx_extractor = DOCXDataExtractor(docx_loader)
    ppt_extractor = PPTDataExtractor(ppt_loader)

    file_storage = FileStorage()
    sql_storage = SQLStorage()

    # Example usage
    file_storage.save_data(pdf_extractor, "sample.pdf")
    sql_storage.save_data(pdf_extractor, "sample.pdf")

    file_storage.save_data(docx_extractor, "sample.docx")
    sql_storage.save_data(docx_extractor, "sample.docx")

    file_storage.save_data(ppt_extractor, "sample.pptx")
    sql_storage.save_data(ppt_extractor, "sample.pptx")

if __name__ == "__main__":
    main()