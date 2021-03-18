import numpy as np
import cv2
from collections import Counter
import mysql.connector
from tkinter import *
import time as t

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

#establishing the connection
conn = mysql.connector.connect(user='root', password='', host='localhost', database='strike_project')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

def login():
    global root2
    root2 = Tk()
    root2.title("Smart Inventory System")
    root2.geometry("750x450")
    root2.config()
    
    global username_verification
    global password_verification
    Label(root2, text='Login', bd=5,font=('arial', 25, 'bold'), relief="groove", fg="black", width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="").pack()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="black", fg='white', relief="groove", font=('arial', 12, 'bold'), command = login_verification).pack()
    Label(root2, text="")

def failed_destroy():
    failed_message.destroy()

def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x200")
    Label(failed_message, text="Invalid Username or Password\n\nOR\n\nYour account doesn't exist.", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="red", fg='white', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()

def logged_destroy():
    logged_message.destroy()
    root2.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome {}".format(username_verification.get()))
    logged_message.geometry("500x310")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold", bd = 5, width = 300).pack()
    Label(logged_message, text="").pack()
    Label(logged_message, text="").pack()
    Label(logged_message, text="").pack()
    Label(logged_message, text="").pack() 
    Label(logged_message, text="To know the live count of stock in your inventory, press this button.", fg="black", font="bold").pack()
    Label(logged_message, text="").pack() 
    Button(logged_message, text="Live Count", bg="black", fg='white', relief="groove", font=('arial', 12, 'bold'), command=live_count).pack()
    Label(logged_message, text="").pack()
    Label(logged_message, text="").pack()
    Label(logged_message, text="").pack() 
    Label(logged_message, text="").pack() 
    Button(logged_message, text="Logout", bg="black", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()

def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    print(user_verification)
    print(pass_verification)
    sql = "select * from client_userdata where username = %s and password = %s"
    cursor.execute(sql,[(user_verification),(pass_verification)])
    results = cursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def live_count():
    cap = cv2.VideoCapture(0)
    i=0
    count_list=[]

    while i < 500:
        # Capture frame-by-frame
        ret, captured_frame = cap.read()
        output_frame = captured_frame.copy()

        # Convert original image to BGR, since Lab is only available from BGR
        captured_frame_bgr = cv2.cvtColor(captured_frame, cv2.COLOR_BGRA2BGR)
        # First blur to reduce noise prior to color space conversion
        captured_frame_bgr = cv2.medianBlur(captured_frame_bgr, 3)
        # Convert to Lab color space, we only need to check one channel (a-channel) for red here
        # captured_frame_lab = cv2.cvtColor(captured_frame_bgr, cv2.COLOR_BGR2Lab)
        hsv = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2HSV)
        # Threshold the Lab image, keep only the red pixels
        # Possible yellow threshold: [20, 110, 170][255, 140, 215]
        # Possible blue threshold: [20, 115, 70][255, 145, 120]
        # captured_frame_lab_red = cv2.inRange(captured_frame_lab, np.array([20, 150, 150]), np.array([190, 255, 255]))
        captured_frame_lab_red = cv2.inRange(hsv, np.array([110, 50, 50]), np.array([130, 255, 255]))
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

    #SELECT id from client_client where user_id = (SELECT id from auth_user where username = username_verification.get())


    mySql_insert_query = """INSERT INTO client_count_table (user, count,accuracy,time_stamp) 
                                    VALUES (%s,%s,%s,%s) """

    record = (username_verification.get(), count2,accuracy,now)



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


login()
root2.mainloop()
# Closing the connection
conn.close()

