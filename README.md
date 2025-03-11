
# Storage Module

This module provides an abstraction for saving data extracted from files using the `DataExtractor` class. It includes two storage implementations: `FileStorage` and `SQLStorage`.

## Classes

### Storage (Abstract Base Class)
An abstract base class that defines the interface for saving data.

#### Methods
- `save_data(data_extractor: DataExtractor, file_path: str)`: Abstract method to save data extracted from the given file path.

### FileStorage
A concrete implementation of `Storage` that saves extracted text and images to the filesystem.

#### Methods
- `save_data(data_extractor: DataExtractor, file_path: str)`: Extracts text and images from the file and saves them to the `output` directory.

### SQLStorage
A concrete implementation of `Storage` that saves extracted text, links, and tables to an SQLite database.

#### Methods
- `save_data(data_extractor: DataExtractor, file_path: str)`: Extracts text, links, and tables from the file and saves them to an SQLite database in the `output` directory.

## Usage

1. Ensure you have a `DataExtractor` class that provides the following methods:
    - `extract_text(file_path: str) -> str`
    - `extract_images(file_path: str) -> List[bytes]`
    - `extract_links(file_path: str) -> List[Tuple[str, str]]`
    - `extract_tables(file_path: str) -> List[Any]`

2. Create an instance of `FileStorage` or `SQLStorage`.

3. Call the `save_data` method with an instance of `DataExtractor` and the file path from which to extract data.

### Example

```python
from data_extractor import DataExtractor
from storage import FileStorage, SQLStorage

data_extractor = DataExtractor()
file_path = 'path/to/your/file'

# Save data to filesystem
file_storage = FileStorage()
file_storage.save_data(data_extractor, file_path)

# Save data to SQLite database
sql_storage = SQLStorage()
sql_storage.save_data(data_extractor, file_path)
```

## Directory Structure

- `output/`: Directory where extracted data will be saved.
  - `text.txt`: File containing extracted text (for `FileStorage`).
  - `image_{idx}.png`: Files containing extracted images (for `FileStorage`).
  - `data.db`: SQLite database containing extracted text, links, and tables (for `SQLStorage`).

## Requirements

- Python 3.x
- `sqlite3` module (included with Python standard library)
- `os` module (included with Python standard library)
- `abc` module (included with Python standard library)
