import cv2
import numpy as np

def detect_defects(edge_img, min_area):
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(edge_img, kernel, iterations=1)
    closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    defect_contours = []
    mask = np.zeros_like(edge_img)

    for cnt in contours:
        if cv2.contourArea(cnt) >= min_area:
            defect_contours.append(cnt)
            cv2.drawContours(mask, [cnt], -1, 255, -1)

    return defect_contours, mask


def classify_defect(mask, threshold_ratio):
    defect_area = (mask > 0).sum()
    total_area = mask.size

    ratio = defect_area / total_area
    is_defect = ratio > threshold_ratio

    return is_defect, ratio
