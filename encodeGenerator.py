import cv2
import face_recognition
import mysql.connector
import pickle
import os

# Function to connect to MySQL database
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

# Function to retrieve image paths from a folder
def retrieve_image_paths(folder_path):
    path_list = os.listdir(folder_path)
    img_list = []
    student_ids = []

    for path in path_list:
        img_list.append(cv2.imread(os.path.join(folder_path, path)))
        student_ids.append(os.path.splitext(path)[0])

    return img_list, student_ids

# Function to encode images using face_recognition library
def find_encodings(images_list):
    encode_list = []
    for img in images_list:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img_rgb)
        if encodings:  # Check if there are any encodings
            encode = encodings[0]  # Assuming only one face per image
            encode_list.append(encode)
        else:
            print("No face found in image.")
    return encode_list

# Function to check if a student ID exists in the Encodings table
def student_id_exists(student_id, cursor):
    query = "SELECT COUNT(*) FROM Encodings WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    return cursor.fetchone()[0] > 0

# Function to save encodings to MySQL database
def save_encodings_to_mysql(encode_list, student_ids):
    try:
        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()

            for encode, student_id in zip(encode_list, student_ids):
                if not student_id_exists(student_id, cursor):
                    encoded_data = pickle.dumps(encode)
                    sql = "INSERT INTO Encodings (student_id, encodings) VALUES (%s, %s)"
                    values = (student_id, encoded_data)
                    cursor.execute(sql, values)
                else:
                    print(f"Student ID {student_id} already exists. Skipping encoding.")

            db_connection.commit()
            cursor.close()
            db_connection.close()
            print("Encodings saved to MySQL successfully!")
        else:
            print("Failed to connect to MySQL database.")
    except mysql.connector.Error as err:
        print(f"Error saving encodings to MySQL: {err}")

# Function to save encodings and student IDs to a pickle file
def save_encodings_to_file(encode_list, student_ids, file_name="EncodeFile.p"):
    try:
        encode_data = [encode_list, student_ids]
        with open(file_name, 'wb') as file:
            pickle.dump(encode_data, file)
        print(f"Encodings and student IDs saved to {file_name} successfully!")
    except Exception as e:
        print(f"Error saving encodings and student IDs to {file_name}: {e}")

# Main script to encode images, save encodings to MySQL, and save to pickle file
def main():
    folder_path = 'Images'  # Replace with your folder containing images
    img_list, student_ids = retrieve_image_paths(folder_path)

    # Print the number of images and student IDs retrieved
    print(f"Number of images: {len(img_list)}")
    print(f"Number of student IDs: {len(student_ids)}")

    encode_list_known = find_encodings(img_list)

    # Print the number of encodings found
    print(f"Number of encodings found: {len(encode_list_known)}")

    # Save encodings to MySQL database
    save_encodings_to_mysql(encode_list_known, student_ids)

    # Save encodings and student IDs to pickle file (optional)
    save_encodings_to_file(encode_list_known, student_ids)

if __name__ == "__main__":
    main()
