from ultralytics import YOLO

# 학습한 모델 로드
model = YOLO("./custom_yolo_train/runs/train/custom_yolov83/weights/best.pt")

# 이미지 예측
# results = model("test_image1.jpeg")
results = model.predict(source="test_image1.jpeg", save=True)

print(results)

# 결과 확인
"""
for result in results:
    boxes = result.boxes.xyxy  # 좌표
    labels = result.boxes.cls  # 클래스 ID
    scores = result.boxes.conf  # Confidence
    print(boxes, labels, scores)
    print(f"labels : {labels}")
"""