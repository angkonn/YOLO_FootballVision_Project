<<<<<<< HEAD

from ultralytics import YOLO

model = YOLO('models/best.pt')

results = model.predict('input_videos/08fd33_4.mp4',save=True)
print(results[0])
print('******************************')
for box in results[0].boxes:
    print(box)


=======
from ultralytics import YOLO

model = YOLO('yolov8x')

results = model.predict('input_videos/08fd33_4.mp4',save=True)
print(results[0])
print('******************************')
for box in results[0].boxes:
    print(box)
>>>>>>> 2589536c06b40dfcd14fd713c4412cb327a3206b
