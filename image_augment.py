# image_augment.py - Image Augmentation Module

import random
from PIL import Image, ImageEnhance

def augment_image(image_path):
    """
    Applies image augmentation techniques to generate variations of the given image.
    Techniques used:
    1. Random rotation (90, 180, 270 degrees)
    2. Horizontal and vertical flipping
    3. Brightness adjustment
    
    Args:
        image_path (str): The path to the image file.
    
    Returns:
        list: A list of augmented images.
    """
    img = Image.open(image_path)
    augmented_images = []

    # Random rotation (90, 180, 270 degrees)
    rotated = img.rotate(random.choice([90, 180, 270]))
    augmented_images.append(rotated)
    
    # Horizontal and vertical flipping
    augmented_images.append(img.transpose(Image.FLIP_LEFT_RIGHT))
    augmented_images.append(img.transpose(Image.FLIP_TOP_BOTTOM))
    
    # Brightness adjustment
    enhancer = ImageEnhance.Brightness(img)
    brightened = enhancer.enhance(random.uniform(0.7, 1.3))
    augmented_images.append(brightened)
    
    return augmented_images