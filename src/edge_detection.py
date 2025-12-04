import cv2
import numpy as np

def detect_edges_canny(gray, low, high):
    """
    Phát hiện biên bằng Canny.
    """
    edges = cv2.Canny(gray, low, high)
    return edges


def detect_edges_sobel(gray):
    """
    Phát hiện biên bằng Sobel (gradient magnitude + threshold).
    """
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    mag = (sobelx ** 2 + sobely ** 2) ** 0.5
    if mag.max() != 0:
        mag = (255 * mag / mag.max()).astype("uint8")
    else:
        mag = mag.astype("uint8")

    _, thresh = cv2.threshold(mag, 50, 255, cv2.THRESH_BINARY)
    return thresh
