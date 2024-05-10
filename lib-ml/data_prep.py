# data_preprocessing.py

import os
import yaml
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from joblib import dump


def load_data(file_path):
    """
    Loads data from file for URL phishing prediction
    Args:
        file_path: Path to txt file with data

    Returns:
        X, Y dataset
    """
    with open(file_path, "r") as file:
        data = [line.strip() for line in file.readlines()]
    x_data = [line.split("\t")[1] for line in data]
    y_data = [line.split("\t")[0] for line in data]
    return x_data, y_data


def preprocess_data(raw_x_train, raw_y_train, raw_x_val, raw_y_val, raw_x_test, raw_y_test):
    """
    Preprocesses data for URL phishing prediction
    Args:
        raw_x_train: list of input train sequences
        raw_y_train: list of output train sequences
        raw_x_val: list of input val sequences
        raw_y_val: list of output val sequences
        raw_x_test: list of input test sequences
        raw_y_test: list of output test sequences

    Returns:
        [x_train, y_train]:
        [x_val, y_val]:
        [x_test, y_test]:
        char_index:
    """
    # Tokenization and Padding
    tokenizer = Tokenizer(lower=True, char_level=True, oov_token='-n-')
    tokenizer.fit_on_texts(raw_x_train + raw_x_val + raw_x_test)
    char_index = tokenizer.word_index
    sequence_length = 200
    x_train = pad_sequences(tokenizer.texts_to_sequences(raw_x_train), maxlen=sequence_length)
    x_val = pad_sequences(tokenizer.texts_to_sequences(raw_x_val), maxlen=sequence_length)
    x_test = pad_sequences(tokenizer.texts_to_sequences(raw_x_test), maxlen=sequence_length)

    # Encoding Labels
    encoder = LabelEncoder()
    y_train = encoder.fit_transform(raw_y_train)
    y_val = encoder.transform(raw_y_val)
    y_test = encoder.transform(raw_y_test)

    return [x_train, y_train], [x_val, y_val], [x_test, y_test], char_index


def save_preprocessed_data(data_path, out_path):
    """
    Read datasets from given path and save them as joblib files in the output path after preprocessing.
    Args:
        data_path: Folder path containing raw data
        out_path: Folder path to save preprocessed data

    Returns:
    """
    train_file = data_path + "train.txt"
    val_file = data_path + "val.txt"
    test_file = data_path + "test.txt"

    raw_x_train, raw_y_train = load_data(train_file)
    raw_x_val, raw_y_val = load_data(val_file)
    raw_x_test, raw_y_test = load_data(test_file)

    ds_train, ds_val, ds_test, char_index = preprocess_data(raw_x_train, raw_y_train,
                                                            raw_x_val, raw_y_val,
                                                            raw_x_test, raw_y_test)

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    dump(ds_train, f'{out_path}ds_train.joblib')
    dump(ds_val, f'{out_path}ds_val.joblib')
    dump(ds_test, f'{out_path}ds_test.joblib')
    dump(char_index, f'{out_path}char_index.joblib')

    print("Done preprocessing data. Exiting data_prep.py")
    return
