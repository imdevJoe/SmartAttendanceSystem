import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import mysql.connector
from datetime import datetime
import subprocess


# def back_click():
#     root.destroy()
#     subprocess.run(["python", "descisionPage.py"])

# MySQL connection configuration
def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="attendance_db"
        )
        return db_connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# Activate webcam and set resolution
camera_capture = cv2.VideoCapture(0)
camera_capture.set(3, 640)
camera_capture.set(4, 480)

# Load background image and status images
imgBackground = cv2.imread('Resources/Drawing4.png')
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = [cv2.imread(os.path.join(folderModePath, path)) for path in modePathList]

# Load encoded data from pickle file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []

# Main loop to capture frames from webcam
while True:
    ret, img = camera_capture.read()

    # Resize and convert frame for face recognition
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Detect faces and encode them
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # Overlay webcam frame on background image
    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                print("Known Face Detected")
                id = studentIds[matchIndex]

                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Strict Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

        if counter != 0:
            if counter == 1:
                # Retrieve student information from MySQL database
                db_connection = connect_to_database()
                if db_connection:
                    cursor = db_connection.cursor(dictionary=True)
                    query = f"SELECT * FROM Students WHERE student_id = '{id}'"
                    cursor.execute(query)
                    studentInfo = cursor.fetchone()

                    if studentInfo:
                        # Download image from MySQL storage (assuming BLOB format)
                        query = f"SELECT image_path FROM Students WHERE student_id = '{id}'"
                        cursor.execute(query)
                        image_path = cursor.fetchone()['image_path']

                        # Load and display student image
                        imgStudent = cv2.imread(image_path)

                        # Update attendance and last attendance time
                        datetimeObject = studentInfo['last_attendance_time']
                        secondsElapsed = (datetime.now() - datetimeObject).total_seconds()

                        if secondsElapsed > 30:
                            new_total_attendance = studentInfo['total_attendance'] + 1
                            query_update = f"UPDATE Students SET total_attendance = {new_total_attendance}, last_attendance_time = '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE student_id = '{id}'"
                            cursor.execute(query_update)
                            db_connection.commit()

                        else:
                            modeType = 3
                            counter = 0
                            imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                    cursor.close()
                    db_connection.close()

            if modeType != 3:
                if 10 < counter < 20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
                if counter <= 10 and 'studentInfo' in locals():  # Check if studentInfo is defined
                    cv2.putText(imgBackground, str(studentInfo['total_attendance']), (861, 125),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(imgBackground, str(studentInfo['course']), (1006, 550),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id), (1006, 493),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['standing']), (910, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo['starting_year']), (1125, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(studentInfo['name']), (808 + offset, 445),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                    imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

                counter += 1

                if counter >= 20:
                    counter = 0
                    modeType = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    else:
        modeType = 0
        counter = 0

    cv2.imshow('Strict Attendance', imgBackground)

    if cv2.waitKey(1) == ord('q'):
        break
# Create a button to move back to the decision page
# backButton = Button(root, text="Back", bg= '#DDA8B5', command=back_click, fg='white', cursor="hand2",font=('lemon juice', 20, 'bold'))
# backButton.place(x=30,y=20)

camera_capture.release()
cv2.destroyAllWindows()
