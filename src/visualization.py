import cv2

def draw_result(img, contours, is_defect, ratio, method: str):
    """
    Vẽ contour vùng lỗi và text trạng thái lên ảnh màu.
    """
    output = img.copy()

    # Vẽ vùng lỗi
    if contours:
        cv2.drawContours(output, contours, -1, (0, 0, 255), 2)

    # Text hiển thị trạng thái
    status = f"DEFECT: {is_defect} (ratio={ratio:.3f}) [{method}]"
    color = (0, 0, 255) if is_defect else (0, 255, 0)

    cv2.putText(
        output,
        status,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        color,
        2,
        lineType=cv2.LINE_AA,
    )

    return output
