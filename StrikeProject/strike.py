import cv2
cap = cv2.VideoCapture('http://192.168.0.103:8080/video')

# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 255, 0)
    gaussian_blur = cv2.GaussianBlur(gray, (21, 21), 0)
    threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1] 
    threshold = cv2.dilate(threshold, None, iterations = 0)
    cnts, _ = cv2.findContours(threshold.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    count = 0
    for c in cnts:
        area = cv2.contourArea(c) 
   
    # Shortlisting the regions based on there area. 
        if area > 700:  
            approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True) 
   
        # Checking if the no. of sides of the selected region is 4. 
            if(len(approx) == 4):  
                cv2.drawContours(frame, [approx], -1, (0, 0, 255), 5)
                count += 1
    #     if cv2.contourArea(c) > 2000:
    #         cv2.drawContours(frame, c, -1, (0, 255, 0), 3)
    #         count += 1
    frame = cv2.putText(frame, 'Number of units - '+str(count), (200, 700) , cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('contours', frame)
    cv2.imshow('threshold', threshold)
    cv2.imshow('gray', gray)

    # for c in cnts:
    #     if cv2.contourArea(c) < 1000:
    #         continue
    #     (x, y, w, h) = cv2.boundingRect(c)
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255, 0), 4)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    


