import cv2 as cv   
import mediapipe as mp 
import time 
import os
import numpy as np


folderpath = "Pic_header"
mylist = os.listdir(folderpath)
#print(mylist)
overlaylist = []

for imgpath in mylist:
    image = cv.imread(f'{folderpath}/{imgpath}')
    overlaylist.append(image)

#print(len(overlaylist))

header = overlaylist[0]
drawcolor = (0,255,0) # green default color
brushthickness = 10
eraserthickness = 100
xp,yp=0,0

cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

framecanvas = np.zeros((720,1280,3),np.uint8)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False,1,0.85)   #hands = mpHands.Hands(static_image_mode=False,
                          #max_num_hands=2,
                          #min_detection_confidence=0.5,
                          #min_tracking_confidence=0.5)
                          
mpDraw = mp.solutions.drawing_utils  # locate 21 points of hand 

ptime = 0
ctime = 0
lmlist=[]
x1,y1,x2,y2=0,0,0,0
tippoint=[4,8,12,16,20]

while True:
    k,frame = cap.read()
    frame = cv.flip(frame,1) # flipping

    imgRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)  -->it checks presence of hand 

    if results.multi_hand_landmarks:

        for handlandmarks in results.multi_hand_landmarks:

            for id,lm in enumerate(handlandmarks.landmark):
                #print(id,lm)
                h,w,c = frame.shape
                cx,cy = int(lm.x*w),int(lm.y*h)   # coordinates of 21 landmarks 
                #print(id,cx,cy) 
                lmlist.append([id,cx,cy])
                    
                if id==8:
                    x1,y1 = cx,cy

                if id==12:
                    x2,y2 = cx,cy    

                    # Two fingers are UP
                    if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2]:
                        xp,yp = 0,0
                        
                        print('Selection Mode')

                        # Checking for the click
                        if y1<171:
                            if 250<x1<450:
                                header = overlaylist[0]
                                drawcolor = (0,255,0)
                            elif 530<x1<700:
                                header = overlaylist[1]
                                drawcolor = (255,0,0)
                            elif 800<x1<970:
                                header = overlaylist[2]
                                drawcolor = (255,0,255)
                            elif 1020<x1<1200:
                                header = overlaylist[3]   
                                drawcolor = (0,0,0)       

                        cv.rectangle(frame,(x1,y1-20),(x2,y2+20),drawcolor,-1)          


                    # Index Finger up and Middle Finger down    
                    if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] > lmlist[10][2]:
                        cv.circle(frame,(x1,y1),15,drawcolor,-1)

                        print('Drawing Mode')  

                        if xp==0 and yp==0:
                            xp,yp = x1,y1
                        
                        if drawcolor==(0,0,0):
                            cv.line(frame,(xp,yp),(x1,y1),drawcolor,eraserthickness)
                            cv.line(framecanvas,(xp,yp),(x1,y1),drawcolor,eraserthickness)
                        
                        else:
                            cv.line(frame,(xp,yp),(x1,y1),drawcolor,brushthickness)
                            cv.line(framecanvas,(xp,yp),(x1,y1),drawcolor,brushthickness)
                        
                        xp,yp = x1,y1
            
            lmlist=[]
            mpDraw.draw_landmarks(frame, handlandmarks, mpHands.HAND_CONNECTIONS)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime 

    cv.putText(frame,str(int(fps)),(30,670),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    
    framegray = cv.cvtColor(framecanvas,cv.COLOR_BGR2GRAY)
    _,frameinv = cv.threshold(framegray,50,255,cv.THRESH_BINARY_INV) # drawing with black brush in white page
    frameinv = cv.cvtColor(frameinv,cv.COLOR_GRAY2BGR)
    frame = cv.bitwise_and(frame,frameinv)
    frame = cv.bitwise_or(frame,framecanvas)

    # Set the header image
    frame[0:171,0:1280] = header
    #frame = cv.addWeighted(frame,0.5,framecanvas,0.5,0)
    cv.imshow('Frame',frame)
    #cv.imshow('Canvas',framecanvas)
    if cv.waitKey(1) & 0xFF==ord('e'):
        break

cap.release()
cv.destroyAllWindows()