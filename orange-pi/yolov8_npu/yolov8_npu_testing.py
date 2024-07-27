import cv2
import time
from yolov8_npu import YOLOv8NPU

model = YOLOv8NPU('./rk3588_npu_models/yolov8n.rknn')

if not model.start_rknnLite():
    print('failed to start npu')
    exit(-1)



vid = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0


while(True):
    new_frame_time = time.time()
    ret, frame = vid.read()

    results = model(frame=frame)

    annotate_frame = model.plot(results)

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time

    fps = int(fps)
    fps_string = str(fps)

    cv2.putText(annotate_frame, fps_string, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', annotate_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


vid.release()
cv2.destroyAllWindows()