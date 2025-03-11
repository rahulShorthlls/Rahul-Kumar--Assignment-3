import unittest
from file_loader import PDFLoader, DOCXLoader, PPTLoader
from data_extractor import PDFDataExtractor, DOCXDataExtractor, PPTDataExtractor

class TestDataExtractor(unittest.TestCase):
    def test_extract_text_pdf(self):
        loader = PDFLoader()
        extractor = PDFDataExtractor(loader)
        self.assertIsNotNone(extractor.extract_text("sample.pdf"))

    def test_extract_text_docx(self):
        loader = DOCXLoader()
        extractor = DOCXDataExtractor(loader)
        self.assertIsNotNone(extractor.extract_text("sample.docx"))

    def test_extract_text_ppt(self):
        loader = PPTLoader()
        extractor = PPTDataExtractor(loader)
        self.assertIsNotNone(extractor.extract_text("sample.pptx"))

    # Add similar tests for extract_links, extract_images, and extract_tables

if __name__ == '__main__':
    unittest.main()
