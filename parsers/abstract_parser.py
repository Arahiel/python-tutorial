import abc


class IParser(metaclass=abc.ABCMeta):
    """Formal IParser interface using abc module"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "load_data_source") and
                callable(subclass.load_data_source) and
                hasattr(subclass, "extract_text") and
                callable(subclass.extract_text)
                )

    @abc.abstractmethod
    def load_data_source(self, file_path: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, file_path: str):
        """Extract text from data set"""
        raise NotImplementedError
