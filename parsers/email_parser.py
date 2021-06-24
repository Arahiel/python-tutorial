from . import IParser


class EmailParser(IParser):
    """Class implementing IParser interface for emails"""
    def load_data_source(self, file_path: str) -> str:
        """Overrides IParser.load_data_source"""
        pass

    def extract_email_text(self, file_path: str) -> dict:
        """Does NOT override IParser.extract_text"""
        pass
