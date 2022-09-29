#One of the image processing project
#edge detection using laplacian method
import cv2 as cv
import numpy as np
camera=cv.VideoCapture(0)
while True:
    _, frame=camera.read()
    cv.imshow("camera",frame)

    laplacian=cv.Laplacian(frame,cv.CV_64F)
    laplacian=np.uint8(laplacian)
    cv.imshow("laplician",laplacian)
    if cv.waitKey(5)==ord("x"):
        break
camera.release()
cv.distroyAllWindows()
