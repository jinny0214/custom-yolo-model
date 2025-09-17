from ultralytics import YOLO

def train_yolo():

    # 모델 로드 (yolov8n, yolov8s, yolov8m, yolov8l, yolov8x 중 선택)
    model = YOLO('yolov8s.pt')  # 경량 네트워크

    # 학습 시작
    results = model.train(
        data='data.yaml',     # 데이터셋 정보 yaml 경로
        epochs=100,           # 학습 epoch 수
        batch=32,             # 배치 사이즈
        imgsz=640,            # 입력 이미지 크기
        project='runs/train', # 결과 저장 폴더
        name='custom_yolov8', # 실험 이름
        device='0',           # GPU 번호, CPU 사용시 'cpu'
        cache=True,            # 데이터셋 캐싱
        workers=8
    )

    return results

if __name__ == "__main__":
    results = train_yolo()
    print(results)