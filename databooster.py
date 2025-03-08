# databoostr.py - Main Package Module

import os
import nltk
from utils import check_data_balance
from image_augment import augment_image
from text_augment import augment_text

nltk.download('wordnet')

class DataBoostr:
    """
    DataBoostr is a Python package for automatic data augmentation.
    It supports both image and text augmentation techniques to balance datasets.
    
    Attributes:
        dataset_path (str): Path to the dataset directory.
        mode (str): The type of data to augment ('image' or 'text').
    """
    
    def __init__(self, dataset_path, mode="image"):
        """
        Initializes the DataBoostr class.
        
        Args:
            dataset_path (str): Path to the dataset directory.
            mode (str, optional): Type of data ('image' or 'text'). Defaults to 'image'.
        """
        self.dataset_path = dataset_path
        self.mode = mode
    
    def check_data_balance(self):
        """
        Checks the class distribution in the dataset.
        
        Returns:
            dict: A dictionary with class labels as keys and sample counts as values.
        """
        return check_data_balance(self.dataset_path)
    
    def auto_augment(self):
        """
        Automatically applies data augmentation based on the selected mode.
        
        Saves augmented images or text files in the same directory as the original data.
        """
        if self.mode == "image":
            for label in os.listdir(self.dataset_path):
                class_dir = os.path.join(self.dataset_path, label)
                if os.path.isdir(class_dir):
                    for img_file in os.listdir(class_dir):
                        img_path = os.path.join(class_dir, img_file)
                        augmented_images = augment_image(img_path)
                        for idx, aug_img in enumerate(augmented_images):
                            aug_img.save(os.path.join(class_dir, f"aug_{idx}_{img_file}"))
        elif self.mode == "text":
            for label in os.listdir(self.dataset_path):
                class_dir = os.path.join(self.dataset_path, label)
                if os.path.isdir(class_dir):
                    for text_file in os.listdir(class_dir):
                        text_path = os.path.join(class_dir, text_file)
                        with open(text_path, "r", encoding="utf-8") as file:
                            text = file.read()
                        augmented_texts = augment_text(text)
                        for idx, aug_text in enumerate(augmented_texts):
                            with open(os.path.join(class_dir, f"aug_{idx}_{text_file}"), "w", encoding="utf-8") as file:
                                file.write(aug_text)
        else:
            print("Unsupported mode! Please choose either 'image' or 'text'.")


