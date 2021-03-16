import numpy as np
import cv2 as cv
import mysql.connector
# img = cv.imread('opencv-logo-white.png',0)
#establishing the connection
conn = mysql.connector.connect(
   user='root', password='', host='localhost', database='mydatabase')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


cap = cv.VideoCapture(0)
while(True):
    _,img=cap.read()
    img1 = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
    
    circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,20,minRadius=0)
    #circles = np.uint16(np.around(circles))
    if circles is not None:
        
        for i in circles[0,:]:
            
            # draw the 
            cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        print(len(circles[0]))
        count1=len(circles[0])
        # Preparing SQL query to INSERT a record into the database.
        mySql_insert_query = """INSERT INTO count_table (id,count) 
                                VALUES (%s,%s) """

        record = (1,count1)



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
        break
            

    
    cv.imshow('detected circles',cimg)

    if cv.waitKey(1)==27:# esc Key
        break
cv.waitKey(0)
cv.destroyAllWindows()



#establishing the connection
# conn = mysql.connector.connect(
#    user='root', password='', host='localhost', database='mydatabase')

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# # Preparing SQL query to INSERT a record into the database.
# insert_stmt = (
#    "INSERT INTO COUNT_TABLE(count)"
#    "VALUES (%s)"
# )
# data = (count1)

# try:
#    # Executing the SQL command
#    cursor.execute(insert_stmt, data)
   
#    # Commit your changes in the database
#    conn.commit()

# except:
#    # Rolling back in case of error
#    conn.rollback()

# print("Data inserted")

# # Closing the connection
# conn.close()
