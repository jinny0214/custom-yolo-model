# MixingBowl - YOLO 기반 음식 재료 객체 인식

YOLO 모델을 활용한 음식 재료 객체 인식 프로젝트입니다. 이미지에서 다양한 음식 재료를 자동으로 탐지하고 분류하는 파이프라인을 제공합니다.

## 주요 기능

- **완전한 훈련 파이프라인**: YOLOv8을 사용한 커스텀 음식 재료 탐지 모델 훈련
- **사전 훈련된 모델**: 추론에 바로 사용 가능한 훈련된 YOLOv8 모델 포함
- **데이터 수집 도구**: simple-image-download와 OIDv4 ToolKit을 통한 자동 이미지 수집
- **다중 클래스 탐지**: 93개 이상의 음식 재료 클래스 지원 (채소, 과일, 단백질 등)
- **간편한 추론**: 이미지에 대한 객체 탐지를 위한 간단한 Python 스크립트
- **체계적인 데이터셋**: YOLO 형식으로 구성된 훈련/검증/테스트 데이터셋

## 설치 방법

### 사전 요구사항
- Python 3.9 이상

### 설치 단계

1. **저장소 클론**
   ```bash
   git clone https://github.com/jinny0214/custom-yolo-model.git
   cd mixingbowl
   ```

2. **가상환경 생성 및 활성화**
   ```bash
   # Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # Linux/Mac
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **필요한 패키지 설치**
   ```bash
   pip install --upgrade pip
   pip install ultralytics simple-image-download opencv-python pyyaml
   ```

## 사용법

### 사전 훈련된 모델로 추론

훈련된 모델을 사용하여 이미지에서 객체 탐지:

```bash
python test.py
```

또는 코드에서 직접 모델 사용:

```python
from ultralytics import YOLO

# 훈련된 모델 로드
model = YOLO("./custom_yolo_train/runs/train/custom_yolov83/weights/best.pt")

# 이미지에 대한 추론 실행
results = model.predict(source="your_image.jpg", save=True)

# 결과 처리
for result in results:
    boxes = result.boxes.xyxy  # 바운딩 박스 좌표
    labels = result.boxes.cls  # 클래스 ID
    scores = result.boxes.conf  # 신뢰도 점수
    print(f"{len(boxes)}개의 객체를 탐지했습니다")
```

### 모델 재학습

자신의 데이터로 모델을 재훈련하려면:

```bash
cd custom_yolo_train
python custom_yolov8_train.py
```

`custom_yolov8_train.py`에서 훈련 매개변수 수정 가능:
- `epochs`: 훈련 에포크 수 (기본값: 100)
- `batch`: 배치 크기 (기본값: 32)
- `imgsz`: 입력 이미지 크기 (기본값: 640)
- `device`: GPU/CPU 선택 ('0'은 GPU, 'cpu'는 CPU)

## 프로젝트 구조

```
mixingbowl/
├── custom_yolo_train/           # YOLO 훈련 설정 및 스크립트
│   ├── custom_yolov8_train.py  # 훈련 스크립트
│   ├── data.yaml               # 데이터셋 설정
│   ├── images/                 # 훈련 이미지 (train/val/test)
│   ├── labels/                 # YOLO 형식 라벨
│   ├── runs/train/             # 훈련 결과 및 모델 가중치
│   │   └── custom_yolov83/weights/
│   │       ├── best.pt         # 최고 성능 모델 가중치
│   │       └── last.pt         # 마지막 에포크 가중치
│   └── *.pt                    # 사전 훈련된 YOLO 모델들
├── OIDv4_ToolKit/              # Open Images Dataset 도구
├── simple_images/              # 카테고리별 수집된 이미지
├── runs/detect/                # 추론 결과
├── classes.txt                 # 재료 클래스 전체 목록
├── test.py                     # 추론 스크립트
├── download_images.py          # 이미지 수집 스크립트
└── README.md
```

## 예시 결과

모델이 탐지할 수 있는 음식 재료들:

- **채소류**: 토마토, 당근, 양파, 마늘, 양배추, 브로콜리 등
- **과일류**: 사과, 바나나, 오렌지, 딸기, 포도 등
- **단백질**: 닭고기, 소고기, 생선, 달걀, 두부 등
- **곡물류**: 쌀, 빵, 파스타, 면 등
- **조미료**: 소금, 후추, 간장, 기름 등

탐지 결과는 `runs/detect/` 디렉토리에 바운딩 박스와 신뢰도 점수와 함께 저장됩니다.

## 요구사항

### Python 의존성
- **ultralytics**: YOLOv8 구현체
- **torch**: PyTorch 딥러닝 프레임워크
- **opencv-python**: 컴퓨터 비전 라이브러리
- **pyyaml**: YAML 설정 파일 지원
- **simple-image-download**: 이미지 수집 유틸리티

### 시스템 요구사항
- **Python**: 3.9 이상
- **RAM**: 8GB 이상 권장
- **GPU**: 훈련 시 CUDA 호환 GPU 권장
- **저장공간**: 데이터셋과 모델을 위한 10GB 이상

### 하드웨어 권장사항
- **훈련**: 8GB 이상 VRAM을 가진 NVIDIA GPU
- **추론**: CPU 또는 2GB 이상 VRAM을 가진 GPU

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## References

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - YOLO 구현체
- [Open Images Dataset v4](https://storage.googleapis.com/openimages/web/index.html) - 데이터셋 소스
- [simple-image-download](https://github.com/rafaelpadilla/recsys-image-downloader) - 이미지 수집 유틸리티

## 📊 모델 성능

훈련된 모델의 성능:
- **클래스 수**: 93개 이상의 음식 재료 카테고리
- **입력 크기**: 640x640 픽셀
- **아키텍처**: YOLOv8s (효율성을 위한 소형 변형)
- **훈련 데이터**: 훈련/검증/테스트 분할이 포함된 커스텀 데이터셋

---