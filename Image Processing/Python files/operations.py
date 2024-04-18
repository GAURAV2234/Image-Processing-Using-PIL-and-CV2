from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import cv2

def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    return grayscale_image

def detect_edges(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    edges_detected_image = grayscale_image.filter(ImageFilter.FIND_EDGES)
    return edges_detected_image

def enhance_image(image_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(2)  # Increase contrast
    return enhanced_image

def smooth_image(image_path):
    image = Image.open(image_path)
    smooth_image = image.filter(ImageFilter.SMOOTH)
    return smooth_image

def adjust_contrast(image_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    contrast_adjusted_image = enhancer.enhance(2)  # Adjust contrast here
    return contrast_adjusted_image

def denoise_image(image_path):
    image = cv2.imread(image_path)
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    denoised_image = Image.fromarray(cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB))
    return denoised_image

def deblur_image(image_path):
    image = cv2.imread(image_path)
    deblurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    deblurred_image = Image.fromarray(cv2.cvtColor(deblurred_image, cv2.COLOR_BGR2RGB))
    return deblurred_image

def contrast_stretching(image_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    contrast_stretched_image = enhancer.enhance(2)  # Stretch contrast
    return contrast_stretched_image

def histogram_equalization(image_path):
    image = cv2.imread(image_path, 0)
    equalized_image = cv2.equalizeHist(image)
    equalized_image = Image.fromarray(equalized_image)
    return equalized_image

def sharpen_image(image_path):
    image = Image.open(image_path)
    sharpened_image = image.filter(ImageFilter.SHARPEN)
    return sharpened_image

def deblur_image_enhanced(image_path):
    image = cv2.imread(image_path)
    gaussian_blur = cv2.GaussianBlur(image, (0, 0), 3)
    alpha = 1.5  # Contrast control
    beta = -0.5  # Brightness control
    deblurred_image = cv2.addWeighted(image, alpha, gaussian_blur, beta, 0)
    deblurred_image = Image.fromarray(cv2.cvtColor(deblurred_image, cv2.COLOR_BGR2RGB))
    return deblurred_image


def sharpen_image_enhanced(image_path):
    image = cv2.imread(image_path)
    # Define a more aggressive sharpening filter.
    sharpen_kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)
    sharpened_image = Image.fromarray(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
    return sharpened_image





