import os
import shutil

def reset_output_dir(base_path: str):
    """
    Xóa thư mục output cũ (nếu có) và tạo mới cấu trúc chuẩn.
    """
    if os.path.exists(base_path):
        shutil.rmtree(base_path)

    os.makedirs(base_path, exist_ok=True)
    os.makedirs(os.path.join(base_path, "edges"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "masks"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "results"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "ok"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "defect"), exist_ok=True)


def load_all_images(input_dir: str):
    """
    Duyệt toàn bộ file ảnh trong input_dir (kể cả subfolder).
    """
    image_files = []
    for root, _, files in os.walk(input_dir):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
                image_files.append(os.path.join(root, f))
    return image_files
