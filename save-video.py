import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_size = (frame_width,frame_height)
fps = 60
file_name = "video\\video.avi"

output = cv2.VideoWriter(file_name,cv2.VideoWriter_fourcc('M','J','P','G'),fps,frame_size)
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow("video from camera pc", frame)
    if ret is True:
        output.write(frame)
    else:
        print('disconected')
        break
    if cv2.waitKey(1) & 0xFF == ord(" "):
        break
    
cap.release()
cv2.destroyAllWindows()