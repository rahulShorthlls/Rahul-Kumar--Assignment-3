import unittest
from data_extractor import PDFDataExtractor, DOCXDataExtractor, PPTDataExtractor
from storage import FileStorage, SQLStorage
from file_loader import PDFLoader, DOCXLoader, PPTLoader

class TestStorage(unittest.TestCase):
    def test_file_storage(self):
        loader = PDFLoader()
        extractor = PDFDataExtractor(loader)
        storage = FileStorage()
        self.assertIsNone(storage.save_data(extractor, "sample.pdf"))

    def test_sql_storage(self):
        loader = PDFLoader()
        extractor = PDFDataExtractor(loader)
        storage = SQLStorage()
        self.assertIsNone(storage.save_data(extractor, "sample.pdf"))

if __name__ == '__main__':
    unittest.main()
