import cv2 as cv   
import mediapipe as mp 
import time 
import os
import numpy as np


folderpath = "Pic_header00"
mylist = os.listdir(folderpath)
print(mylist)
overlaylist = []

for imgpath in mylist:
    image = cv.imread(f'{folderpath}/{imgpath}')
    overlaylist.append(image)

#print(len(overlaylist))

header = overlaylist[0]
drawcolor = (0,0,255) # green default color
shape = "freestyle"
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
x0,y0,x1,y1,x2,y2=0,0,0,0,0,0
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

                if id==4:
                    x0,y0 = cx,cy

                if id==8:
                    x1,y1 = cx,cy

                if id==12:
                    x2,y2 = cx,cy    

                if id==20:

                    # Two fingers are UP
                    if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2]:
                        xp,yp = 0,0
                        
                        print('Selection Mode')

                        # Checking for the click
                        if y1<172:
                            if 300<x1<420:
                                header = overlaylist[0]
                                drawcolor = (0,0,255)
                            elif 430<x1<570:
                                header = overlaylist[16]
                                drawcolor = (0,255,0)
                            elif 590<x1<720:
                                header = overlaylist[20]
                                drawcolor = (255,0,0)
                            elif 730<x1<870:
                                header = overlaylist[4]   
                                drawcolor = (255,0,255)       
                            elif 900<x1<1020:
                                header = overlaylist[8]   
                                drawcolor = (255,255,0)   
                            elif 1050<x1<1200:
                                header = overlaylist[13]   
                                drawcolor = (0,0,0)         

                        if y1<172 and x1<270 :

                            if (82<y1<172 and 130<x1<260) and drawcolor==(0,0,255):
                                header = overlaylist[0]
                                shape = 'freestyle'
                            elif (82<y1<172 and 0<x1<128) and drawcolor==(0,0,255):
                                header = overlaylist[15]
                                shape = 'ellipse'
                            elif (0<y1<82 and 130<x1<260) and drawcolor==(0,0,255):
                                header = overlaylist[11]
                                shape = 'circle'
                            elif (0<y1<82 and 0<x1<128) and drawcolor==(0,0,255):
                                header = overlaylist[14]
                                shape = 'rectangle'

                            elif (82<y1<172 and 130<x1<260) and drawcolor==(0,255,0):
                                header = overlaylist[16]
                                shape = 'freestyle'
                            elif (82<y1<172 and 0<x1<128) and drawcolor==(0,255,0):
                                header = overlaylist[19]
                                shape = 'ellipse'
                            elif (0<y1<82 and 130<x1<260) and drawcolor==(0,255,0):
                                header = overlaylist[17]
                                shape = 'circle'
                            elif (0<y1<82 and 0<x1<128) and drawcolor==(0,255,0):
                                header = overlaylist[18]
                                shape = 'rectangle'    

                            elif (82<y1<172 and 130<x1<260) and drawcolor==(255,0,0):
                                header = overlaylist[20]
                                shape = 'freestyle'
                            elif (82<y1<172 and 0<x1<128) and drawcolor==(255,0,0):
                                header = overlaylist[3]
                                shape = 'ellipse'
                            elif (0<y1<82 and 130<x1<260) and drawcolor==(255,0,0):
                                header = overlaylist[1]
                                shape = 'circle'
                            elif (0<y1<82 and 0<x1<128) and drawcolor==(255,0,0):
                                header = overlaylist[2]
                                shape = 'rectangle'    

                            elif (82<y1<172 and 130<x1<260) and drawcolor==(255,0,255):
                                header = overlaylist[4]
                                shape = 'freestyle'
                            elif (82<y1<172 and 0<x1<128) and drawcolor==(255,0,255):
                                header = overlaylist[7]
                                shape = 'ellipse'
                            elif (0<y1<82 and 130<x1<260) and drawcolor==(255,0,255):
                                header = overlaylist[5]
                                shape = 'circle'
                            elif (0<y1<82 and 0<x1<128) and drawcolor==(255,0,255):
                                header = overlaylist[6]
                                shape = 'rectangle'     
                            
                            elif (82<y1<172 and 130<x1<260) and drawcolor==(255,255,0):
                                header = overlaylist[8]
                                shape = 'freestyle'
                            elif (82<y1<172 and 0<x1<128) and drawcolor==(255,255,0):
                                header = overlaylist[12]
                                shape = 'ellipse'
                            elif (0<y1<82 and 130<x1<260) and drawcolor==(255,255,0):
                                header = overlaylist[9]
                                shape = 'circle'
                            elif (0<y1<82 and 0<x1<128) and drawcolor==(255,255,0):
                                header = overlaylist[10]
                                shape = 'rectangle' 


                        cv.rectangle(frame,(x1,y1-20),(x2,y2+20),drawcolor,-1)          


                    # Index Finger up and Middle Finger down    
                    if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] > lmlist[10][2]:
                        cv.circle(frame,(x1,y1),15,drawcolor,-1)

                        print('Drawing Mode')  

                        if xp==0 and yp==0:
                            xp,yp = x1,y1
                        
                        if drawcolor==(0,0,0):
                            eraserthickness = 50
                            
                            result = int(((((x0 - x1) ** 2) + ((y0 - y1) ** 2)) ** 0.5))

                            if result<0:
                                result = -1 * result

                            new_eraserthickness = result

                            if lmlist[8][2] < lmlist[6][2] and lmlist[20][2] < lmlist[18][2]:
                                eraserthickness = new_eraserthickness

                            
                            cv.line(frame,(xp,yp),(x1,y1),drawcolor,eraserthickness)
                            cv.line(framecanvas,(xp,yp),(x1,y1),drawcolor,eraserthickness)
                        
                        else:

                            if shape == "freestyle":
                                
                                cv.line(frame,(xp,yp),(x1,y1),drawcolor,brushthickness)
                                cv.line(framecanvas,(xp,yp),(x1,y1),drawcolor,brushthickness)
                            
                            if shape == "rectangle":
                                cv.rectangle(frame, (x0, y0), (x1, y1), drawcolor)

                                if lmlist[20][2] < lmlist[18][2]:
                                    cv.rectangle(framecanvas, (x0, y0), (x1, y1), drawcolor)

                            if shape =="circle":
                                
                                result = int(((((x0 - x1) ** 2) + ((y0 - y1) ** 2)) ** 0.5))
                                #print(result)
                                
                                cv.circle(frame,(x1,y1),result,drawcolor)
                                if lmlist[20][2] < lmlist[18][2]:
                                    cv.circle(framecanvas,(x1,y1),result,drawcolor)

                            if shape == "ellipse":
                                a = x0-x1
                                b = y0-x2        

                                if x1>250:
                                    b=int(b/2)

                                if a<0:
                                    a=-1*a

                                if b<0:
                                    b=-1*b 

                                cv.ellipse(frame, (x1, y1),(a,b), 0, 0, 360, (0,255,255), 1)    
                                if lmlist[20][2] < lmlist[18][2]:
                                    cv.ellipse(framecanvas, (x1, y1), (a, b), 0, 0, 360, (0,255,255), 1)

                        xp,yp = x1,y1

                    # Clear Canvas when index finger and thumb are down and three fingers are up 
                    if lmlist[8][2] > lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and  lmlist[16][2] < lmlist[14][2] and lmlist[20][2] < lmlist[18][2]:
                        framecanvas = np.zeros((720,1280,3),np.uint8)      
            
            lmlist=[]
            mpDraw.draw_landmarks(frame, handlandmarks, mpHands.HAND_CONNECTIONS)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime 

    cv.putText(frame,str(int(fps)),(30,670),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    cv.putText(frame,'R',(350,200),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv.putText(frame,'G',(500,200),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    cv.putText(frame,'B',(660,200),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
    cv.putText(frame,'M',(830,200),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,255),3)
    cv.putText(frame,'C',(980,200),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0),3)
    cv.putText(frame,'E',(11200,200),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)

    
    framegray = cv.cvtColor(framecanvas,cv.COLOR_BGR2GRAY)
    _,frameinv = cv.threshold(framegray,50,255,cv.THRESH_BINARY_INV) # drawing with black brush in white page
    frameinv = cv.cvtColor(frameinv,cv.COLOR_GRAY2BGR)
    frame = cv.bitwise_and(frame,frameinv)
    frame = cv.bitwise_or(frame,framecanvas)

    # Set the header image
    frame[0:172,0:1280] = header
    #frame = cv.addWeighted(frame,0.5,framecanvas,0.5,0)
    cv.imshow('Frame',frame)
    #cv.imshow('Canvas',framecanvas)
    if cv.waitKey(1) & 0xFF==ord('e'):
        break

cap.release()
cv.destroyAllWindows()