import cv2 as cv

cv.namedWindow('face.exe')

cap = cv.VideoCapture(0)

cap.set(3, 600)
cap.set(4, 600)
cap.set(5, 24)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

running = True

while (running):
    _, vid = cap.read()
    gray = cv.cvtColor(vid, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)

    for (x, y, w, h) in faces:
        cv.circle(vid, (x+w//2, y+h//2), w//2, (0, 0, 255), 2)

    cv.imshow('face.exe', vid)

    esc = cv.waitKey(10)

    if esc == 27: break

cap.release()
cv.destroyAllWindows()