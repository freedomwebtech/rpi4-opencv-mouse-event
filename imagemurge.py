import cv2
import numpy as np
drawing = False
pt1_x , pt1_y = None , None

def line_drawing(event,x,y,flags,param):
    global pt1_x,pt1_y,drawing

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        pt1_x,pt1_y=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.line(img,(pt1_x,pt1_y),(x,y),color=(255,255,255),thickness=3)
            pt1_x,pt1_y=x,y
            print(pt1_x,pt1_y) 
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.line(img,(pt1_x,pt1_y),(x,y),color=(255,255,255),thickness=3)
        pt1_x,pt1_y=x,y
        print(x,y)





cap = cv2.VideoCapture(0)

img = np.zeros((480, 640, 3), np.uint8)
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',line_drawing)
while True:
    ret, frame = cap.read()
    flipped = cv2.flip(frame, flipCode = -1)
    frame1 = cv2.resize(flipped, (640, 480))
    dist = cv2.addWeighted(frame1,0.8,img,0.8,0.5)
#    cv2.imshow("Frame2",frame1)
#    cv2.imshow("Frame1",img)
    cv2.imshow("Frame",dist)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
    
    