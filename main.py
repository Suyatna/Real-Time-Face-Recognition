import numpy as np
import time
import cv2

cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
capture = cv2.VideoCapture(0)

cv2.namedWindow('frame')

while True:
    # capture frame-by-frame
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        print(x, y, w, h)

        # (ycord_start, ycord_end)
        crop_gray = gray[y:y + h, x:x + w]
        crop_color = frame[y:y + h, x:x + w]
        img_item = "my-image.png"
        cv2.imwrite(img_item, crop_gray)

        color = (255, 0, 0)  # BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    if cv2.getWindowProperty('frame', 1) < 0:
        break

# when everything done, release the capture
capture.release()
cv2.destroyAllWindows()
