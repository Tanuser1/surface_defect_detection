import cv2

def preprocess_image(img, resize_width):
    """Resize + grayscale + Gaussian blur"""
    h, w = img.shape[:2]
    scale = resize_width / w
    resized = cv2.resize(img, (resize_width, int(h * scale)))

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)

    return resized, gray_blur
