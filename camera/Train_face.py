import cv2
import face_recognition
import pickle
import os
import requests
from dotenv import dotenv_values

env_values = dotenv_values(os.path.join(os.getcwd(), ".env"))

photo_folder = os.path.join(os.getcwd(), "Face_images/")
facial_encodings_folder = os.path.join(os.getcwd(), "Face_encodings/")

def Send_new_face(name):
    url = env_values["BACKEND"] + "/new_face"
    data = {"name": name}
    try:
        requests.post(url, json=data)
    except Exception as e:
        print(f"An error occurred while sending the request: {e}")

def encoding_of_person_by_image(name, image):
    encoding = []
    img = cv2.imread(image)
    rgb_im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encoding.append(face_recognition.face_encodings(rgb_im)[0])

    with open(facial_encodings_folder + name + ".txt", "wb") as fp:
        pickle.dump(encoding, fp)


def encoding_of_person_by_camera(name):
    encoding = []
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        rgb_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow("frame", frame)
        
        encoding.append(face_recognition.face_encodings(rgb_im))
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    with open(facial_encodings_folder + name + ".txt", "wb") as fp:
        pickle.dump(encoding, fp)


def train_faces_on_folder():
    for file in os.listdir(photo_folder):
        if file.endswith(".jpg"):
            name = file.split(".")[0]
            image = photo_folder + file
            encoding_of_person_by_image(name, image)
            Send_new_face(name)


if __name__ == "__main__":
    train_option = input(
        "Enter 'C' to train using camera or 'F' to train using folder: "
    )

    if train_option == "C" or train_option == "c":
        name = input("Enter the name of the person: ")
        encoding_of_person_by_camera(name)
        Send_new_face(name)
    elif train_option == "F" or train_option == "f":
        train_faces_on_folder()
    else:
        print("Invalid option. Please try again.")
    print("Training completed")
