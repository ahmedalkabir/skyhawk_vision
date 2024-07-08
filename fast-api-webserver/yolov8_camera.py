import cv2
from ultralytics import YOLO
import torch
from imutils.video import FPS
import time

model = YOLO("yolov8s.pt")
# model.export(format="coreml")
coreml_model = YOLO("yolov8s.mlpackage")

vid = cv2.VideoCapture(0)
print(f'MPS: {torch.backends.mps.is_available()}')

def resize_image(frame, width):
    r = width / frame.shape[1]
    dim = (int(width), int(frame.shape[0] * r))
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

# used to record the time when we processed last frame 
prev_frame_time = 0
  
# used to record the time at which we processed current frame 
new_frame_time = 0

fps = FPS()
# fps = fps.start()
while(True):
    # fps = fps.start()
    new_frame_time = time.time() 

    ret, frame = vid.read()

    # Run YOLOv8 inference on the frame
    results = coreml_model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    resized_frame = resize_image(annotated_frame.copy(), 640)

  
    # Calculating the fps 
  
    # fps will be number of frame processed in given time frame 
    # since their will be most of time error of 0.001 second 
    # we will be subtracting it to get more accurate result 
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time 
  
    # converting the fps into integer 
    fps = int(fps) 
  
    # converting the fps to string so that we can display it on frame 
    # by using putText function 
    fps_string = str(fps) 

    # fps.stop()

    # fps_string = str(fps.fps())


    cv2.putText(resized_frame, fps_string, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('resized frame', resized_frame)
    # cv2.imshow('frame', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



fps.stop()
vid.release()
cv2.destroyAllWindows()