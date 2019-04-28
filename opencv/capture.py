import cv2
#cap = cv2.VideoCapture('http://hoge:hoge@localhost:8080/?action=stream')
cap = cv2.VideoCapture('http://hoge:hoge@192.168.1.98:8080/?action=stream')

while True:
  ret, frame = cap.read()
  cv2.imshow('Video', frame)

  # フレームの加工
  # edframe = frame
  laplacian = cv2.Laplacian(frame,cv2.CV_64F)
  ret, threhold = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
  cv2.imshow('Edited Frame', laplacian)
  cv2.imshow('threashold', threhold)

  if cv2.waitKey(1) == 27:
    exit(0)