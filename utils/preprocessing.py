import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Loads an image and applies thresholding to remove noise.
    """
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Gaussian Blur to remove noise
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    
    # Apply Adaptive Thresholding (makes text stand out)
    processed_img = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    
    return processed_img