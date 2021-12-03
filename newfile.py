import cv2
import datetime

cap=cv2.VideoCapture(r"C:\Users\20pa1\Downloads\London Walk from Oxford Street to Carnaby Street.mp4" , 0)

while True:
        
        ret , frame=cap.read()
        
        frame=cv2.resize(frame , (700 , 450))
        gar=cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

        blur=cv2.GaussianBlur(gar, (5 , 5) , 0)

        date_data="Date :" +str(datetime.datetime.now())



        
        font=cv2.FONT_HERSHEY_COMPLEX_SMALL
        
        
        frame=cv2.putText(frame , date_data , (20 ,50 ) , font , 1 , (100 , 289 , 289) , 0)

        gar=cv2.putText(gar, date_data , (20 ,55 ) , font , 1 , (100 , 890, 289) , 0)


        ret , thresh=cv2.threshold(blur , 127 , 255 , 0 , cv2.THRESH_BINARY)
        
        contours= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
       
        
        
        for c in contours:

            cv2.drawContours(frame, [c], -1, (0, 200 , 156), 2)
            
        cv2.imshow("vid",frame)
        

        
        
        
        if cv2.waitKey(1) & 0xFF==ord("s"):
            
            break
        
cap.release()
cv2.destroyAllWindows()



