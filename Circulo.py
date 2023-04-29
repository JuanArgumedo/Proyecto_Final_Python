import cv2 as cv
import numpy as np 

imagen = 255*np.ones((400,600,3),dtype=np.uint8)

cv.circle(imagen,(300,200),100,(255,255,0),-1)

cv.imshow('imagen', imagen)
cv.waitKey(0)
cv.destroyAllWindows()
