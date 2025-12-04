import os
import cv2
import pandas as pd

from config import *
from preprocessing import preprocess_image
from edge_detection import detect_edges_canny, detect_edges_sobel
from defect_detection import detect_defects, classify_defect
from io_utils import reset_output_dir, load_all_images
from visualization import draw_result


def main():
    print("🚀 Surface Defect Detection Running...")

    # 1. Xóa & tạo lại thư mục outputs
    reset_output_dir(OUTPUT_DIR)

    # 2. Lấy danh sách ảnh cần xử lý
    image_paths = load_all_images(INPUT_DIR)
    if not image_paths:
        print("⚠️ Không tìm thấy ảnh nào trong thư mục:", INPUT_DIR)
        return

    results = []

    for img_path in image_paths:
        print("🔍 Processing:", img_path)

        img = cv2.imread(img_path)
        if img is None:
            print("⚠️  Không đọc được ảnh:", img_path)
            continue

        # 3. Tiền xử lý
        resized, gray_blur = preprocess_image(img, RESIZE_WIDTH)

        # 4. Phát hiện biên
        if METHOD.lower() == "canny":
            edges = detect_edges_canny(gray_blur, CANNY_LOW, CANNY_HIGH)
        else:
            edges = detect_edges_sobel(gray_blur)

        # 5. Tìm vùng lỗi + mask
        contours, mask = detect_defects(edges, MIN_DEFECT_AREA)
        is_defect, ratio = classify_defect(mask, AREA_THRESHOLD_RATIO)

        # 6. Vẽ kết quả
        result_img = draw_result(resized, contours, is_defect, ratio, METHOD)

        # 7. Lưu với đuôi .png
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        out_name = base_name + ".png"

        cv2.imwrite(os.path.join(OUTPUT_DIR, "edges", out_name), edges)
        cv2.imwrite(os.path.join(OUTPUT_DIR, "masks", out_name), mask)
        cv2.imwrite(os.path.join(OUTPUT_DIR, "results", out_name), result_img)

        if is_defect:
            cv2.imwrite(os.path.join(OUTPUT_DIR, "defect", out_name), result_img)
        else:
            cv2.imwrite(os.path.join(OUTPUT_DIR, "ok", out_name), result_img)

        results.append([out_name, is_defect, ratio, METHOD])

    # 8. Ghi file CSV kết quả
    df = pd.DataFrame(results, columns=["file", "is_defect", "ratio", "method"])
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(os.path.join(OUTPUT_DIR, "report.csv"), index=False, encoding="utf-8-sig")

    print("✅ DONE! Kết quả đã lưu trong thư mục 'outputs/'")


if __name__ == "__main__":
    main()
