from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from sklearn.preprocessing import LabelEncoder


class TokenizeQuery:
    def __init__(self, word_set: dict = None):
        """
        Takes word_set as input and creates a Tokenizer object to tokenize queries.
        Args:
            word_set: Dictionary of words and their indices
        """
        self.tokenizer = Tokenizer(lower=True, char_level=True, oov_token='-n-')
        if self.word_set:
            self.word_set = word_set
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

    def preprocess_data(self, raw_x_train, raw_y_train, raw_x_val, raw_y_val, raw_x_test, raw_y_test):
        # Tokenization and Padding
        self.tokenizer.fit_on_texts(raw_x_train + raw_x_val + raw_x_test)
        char_index = self.tokenizer.word_index
        sequence_length = 200
        x_train = pad_sequences(self.tokenizer.texts_to_sequences(raw_x_train), maxlen=sequence_length)
        x_val = pad_sequences(self.tokenizer.texts_to_sequences(raw_x_val), maxlen=sequence_length)
        x_test = pad_sequences(self.tokenizer.texts_to_sequences(raw_x_test), maxlen=sequence_length)

        # Encoding Labels
        encoder = LabelEncoder()
        y_train = encoder.fit_transform(raw_y_train)
        y_val = encoder.transform(raw_y_val)
        y_test = encoder.transform(raw_y_test)

        return [x_train, y_train], [x_val, y_val], [x_test, y_test], char_index