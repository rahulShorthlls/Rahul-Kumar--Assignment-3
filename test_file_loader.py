import unittest
from file_loader import PDFLoader, DOCXLoader, PPTLoader

class TestFileLoader(unittest.TestCase):
    def test_pdf_loader(self):
        loader = PDFLoader()
        self.assertTrue(loader.validate_file("sample.pdf"))
        self.assertIsNotNone(loader.load_file("sample.pdf"))

    def test_docx_loader(self):
        loader = DOCXLoader()
        self.assertTrue(loader.validate_file("sample.docx"))
        self.assertIsNotNone(loader.load_file("sample.docx"))

    def test_ppt_loader(self):
        loader = PPTLoader()
        self.assertTrue(loader.validate_file("sample.pptx"))
        self.assertIsNotNone(loader.load_file("sample.pptx"))

if __name__ == '__main__':
    unittest.main()
