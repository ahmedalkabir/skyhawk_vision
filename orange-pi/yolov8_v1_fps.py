from ultralytics import YOLO
import cv2
import time


model = YOLO("yolov8n.pt")
model.to('cuda')
# model.export(format="ncnn")

# ncnn_model = YOLO("yolov8n_ncnn_model")

vid = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0

while(True):
    new_frame_time = time.time()
    ret, frame = vid.read()

    results = model(frame)

    annotate_frame = results[0].plot()

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