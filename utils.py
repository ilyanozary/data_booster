# utils.py - Data Distribution Analysis Module

import os

def check_data_balance(dataset_path):
    """
    Analyzes the distribution of classes in a dataset.
    
    Args:
        dataset_path (str): Path to the dataset directory.
    
    Returns:
        dict: A dictionary with class labels as keys and the number of samples as values.
    """
    class_counts = {}
    for label in os.listdir(dataset_path):
        class_dir = os.path.join(dataset_path, label)
        if os.path.isdir(class_dir):
            class_counts[label] = len(os.listdir(class_dir))
    return class_counts