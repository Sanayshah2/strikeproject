import numpy as np
import cv2
from collections import Counter
import mysql.connector


#establishing the connection
conn = mysql.connector.connect(
   user='root', password='', host='localhost', database='strike_project')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

cap = cv2.VideoCapture(0)
i=0
count_list=[]

while i < 100:
    # Capture frame-by-frame
    ret, captured_frame = cap.read()
    output_frame = captured_frame.copy()

    # Convert original image to BGR, since Lab is only available from BGR
    captured_frame_bgr = cv2.cvtColor(captured_frame, cv2.COLOR_BGRA2BGR)
    # First blur to reduce noise prior to color space conversion
    captured_frame_bgr = cv2.medianBlur(captured_frame_bgr, 3)
    # Convert to Lab color space, we only need to check one channel (a-channel) for red here
    captured_frame_lab = cv2.cvtColor(captured_frame_bgr, cv2.COLOR_BGR2Lab)
    # Threshold the Lab image, keep only the red pixels
    # Possible yellow threshold: [20, 110, 170][255, 140, 215]
    # Possible blue threshold: [20, 115, 70][255, 145, 120]
    captured_frame_lab_red = cv2.inRange(captured_frame_lab, np.array([20, 150, 150]), np.array([190, 255, 255]))
    # Second blur to reduce more noise, easier circle detection
    captured_frame_lab_red = cv2.GaussianBlur(captured_frame_lab_red, (5, 5), 2, 2)
    # Use the Hough transform to detect circles in the image
    circles = cv2.HoughCircles(captured_frame_lab_red, cv2.HOUGH_GRADIENT, 1, captured_frame_lab_red.shape[0] / 8, param1=100, param2=18, minRadius=5, maxRadius=60)
	# If we have extracted a circle, draw an outline
	# We only need to detect one circle here, since there will only be one reference object
    if circles is not None:
        i+=1
        count_list.append(len(circles[0]))
        print(len(circles[0]))
        for x in circles[0]:
            cv2.circle(output_frame, center=(x[0], x[1]), radius=x[2], color=(0, 255, 0), thickness=2)

    # Display the resulting frame, quit with q
    cv2.imshow('frame', output_frame)
    if cv2.waitKey(1)==27:# esc Key
        print('Me hoon')
        print(count_list)
        break

# When everything done, release the capture
print(count_list)
l=Counter(count_list)
print(l)
max1=l.most_common(1)
count2=max1[0][0]
accuracy=max1[0][1]
# max_count=max(lst,key=lst.count)
cap.release()
cv2.destroyAllWindows()

mySql_insert_query = """INSERT INTO client_count_table (count,accuracy) 
                                VALUES (%s,%s) """

record = (count2,accuracy)



try:
# Executing the SQL command
    cursor.execute(mySql_insert_query, record)

# Commit your changes in the database
    conn.commit()
    print('Sucess')

except:
# Rolling back in case of error
    conn.rollback()
    print('Failure')


# Closing the connection
conn.close()

