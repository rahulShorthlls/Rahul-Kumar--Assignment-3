from abc import ABC, abstractmethod
import PyPDF2
import docx
from pptx import Presentation

class FileLoader(ABC):
    @abstractmethod
    def validate_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def load_file(self, file_path: str):
        pass

class PDFLoader(FileLoader):
    def validate_file(self, file_path: str) -> bool:
        return file_path.endswith('.pdf')

    def load_file(self, file_path: str):
        file = open(file_path, 'rb')
        reader = PyPDF2.PdfReader(file)
        return reader, file

class DOCXLoader(FileLoader):
    def validate_file(self, file_path: str) -> bool:
        return file_path.endswith('.docx')

    def load_file(self, file_path: str):
        return docx.Document(file_path)

class PPTLoader(FileLoader):
    def validate_file(self, file_path: str) -> bool:
        return file_path.endswith('.pptx')

    def load_file(self, file_path: str):
        return Presentation(file_path)
