import os
import shutil

src_base = r"C:\Users\Admin\Desktop\dev\mixingbowl\OIDv4_ToolKit\OUTPUT\To_Yolo"
dst_base = r"C:\Users\Admin\Desktop\dev\mixingbowl\custom_yolo_train\labels"

folder_map = {
    'test': 'test',
    'train': 'train',
    'validation': 'val'
}

for src_folder, dst_folder in folder_map.items():
    src_path = os.path.join(src_base, src_folder)
    dst_path = os.path.join(dst_base, dst_folder)
    os.makedirs(dst_path, exist_ok=True)

    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.lower().endswith('.txt'):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_path, file)

                # 파일명 중복 방지
                if os.path.exists(dst_file):
                    base, ext = os.path.splitext(file)
                    count = 1
                    new_name = f"{base}_{count}{ext}"
                    dst_file = os.path.join(dst_path, new_name)
                    while os.path.exists(dst_file):
                        count += 1
                        new_name = f"{base}_{count}{ext}"
                        dst_file = os.path.join(dst_path, new_name)

                shutil.copy2(src_file, dst_file)

    print(f"[INFO] {src_folder} 폴더 내 모든 라벨 파일이 {dst_folder} 폴더로 복사 완료")