"""
This module downloads the dataset from kaggle and stores it in the data folder.
"""
import os
import kaggle
import yaml


def get_data(folder_path: str, kaggle_path: str):
    """
    This function downloads the dataset from kaggle and stores it in the specified folder.
    Args:
        folder_path: Path where the dataset is stored.
        kaggle_path: Kaggle dataset URL used for downloading.

    Returns:
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.chmod("..", 0o777)
        os.makedirs(folder_path)

    # Download the dataset using the Kaggle API
    kaggle.api.dataset_download_files(kaggle_path, path=folder_path, unzip=True)
    return
