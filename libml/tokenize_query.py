from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences


class TokenizeQuery:
    def __init__(self, word_set: dict):
        """
        Takes word_set as input and creates a Tokenizer object to tokenize queries.
        Args:
            word_set: Dictionary of words and their indices
        """
        self.word_set = word_set
        self.tokenizer = Tokenizer(lower=True, char_level=True, oov_token='-n-')
        self.tokenizer.word_index = self.word_set

    def tokenize(self, query: str, sequence_length: int) -> list:
        """

        Args:
            sequence_length: Final length of tokenized query
            query: Text query

        Returns:

        """
        tokenized_query = self.tokenizer.texts_to_sequences([query])
        padded = pad_sequences(tokenized_query, maxlen=sequence_length)
        return padded
