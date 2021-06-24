from . import IParser


class PdfParser(IParser):
    """Class implementing IParser interface for pdf files"""
    def load_data_source(self, file_path: str) -> str:
        """Overrides IParser.load_data_source"""
        pass

    def extract_text(self, file_path: str) -> dict:
        """Overrides IParser.extract_text"""
        pass
