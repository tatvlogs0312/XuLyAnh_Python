import cv2

video = cv2.VideoCapture("video\\myheroacademia3.mp4")
while (True):
    ret, frame = video.read()
    tshape = frame.shape
    cv2.imshow("video from camera pc", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()