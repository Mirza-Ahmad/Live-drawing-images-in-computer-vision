import cv2
import numpy as np 
#Now create the own image without using an image
img=cv2.imread('/computer vision/image/first.png')
def draw(event,x,y,flags,params):
 if event==1:
  cv2.circle(img, center=(x,y), radius=50, color=(0,0,255), thickness=2)
cv2.namedWindow(winname='window')
cv2.setMouseCallback('window', draw)
while True:
 cv2.imshow('window', img)
 if cv2.waitKey(1) & 0xFF==ord('q'):
  break
cv2.destroyAllWindows()