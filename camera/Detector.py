import cv2
import face_recognition
import pickle
import os
import requests
from dotenv import dotenv_values

env_values = dotenv_values(os.path.join(os.getcwd(), ".env"))

known_face_encodings = []
known_face_names = []
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

photo_folder = os.path.join(os.getcwd(), "Face_images/")
facial_encodings_folder = os.path.join(os.getcwd(), "Face_encodings/")
face_set = set()

def Send_located_face(name):
    url = env_values["BACKEND"] + "/located_faces"
    data = {"name": name, "location": "CamJAN"}
    try:
        requests.post(url, json=data)
    except Exception as e:
        print(f"An error occurred while sending the request: {e}")


def load_facial_encodings_and_names_from_memory():
    for filename in os.listdir(facial_encodings_folder):
        known_face_names.append(filename[:-4])
        with open(facial_encodings_folder + filename, "rb") as fp:
            known_face_encodings.append(pickle.load(fp)[0])


def cam_check():
    load_facial_encodings_and_names_from_memory()
    while True:
        ret, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding, tolerance=0.5
            )
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                if name not in face_set:
                    Send_located_face(name)
                    face_set.clear()
                    face_set.add(name)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(
                frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED
            )
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(
                frame, name, (left + 6, bottom - 6), font, .7, (255, 255, 255), 1
            )
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    cam_check()
