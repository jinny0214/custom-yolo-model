import os
import shutil

src_base = r"C:\Users\Admin\Desktop\dev\mixingbowl\OIDv4_ToolKit\OUTPUT\To_Yolo"
dst_base = r"C:\Users\Admin\Desktop\dev\mixingbowl\custom_yolo_train\labels"

folder_map = {
    'test': 'test',
    'train': 'train',
    'validation': 'val'  # validation → val
}

for src_folder, dst_folder in folder_map.items():
    src_path = os.path.join(src_base, src_folder)
    dst_path = os.path.join(dst_base, dst_folder)
    os.makedirs(dst_path, exist_ok=True)

    # os.walk를 사용해 하위 폴더 포함 탐색
    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_path, file)

                # 동일 이름 파일 충돌 시 덮어쓰기 방지
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

    print(f"[INFO] {src_folder} 내 모든 이미지가 {dst_folder} 폴더로 복사 완료")