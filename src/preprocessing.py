import cv2

def preprocess_image(img, resize_width):
    """Resize + grayscale + Gaussian blur"""
    h, w = img.shape[:2]
    scale = resize_width / w
    img_resized = cv2.resize(img, (resize_width, int(h * scale)))

    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)

    return img_resized, gray_blur
