# Todos:

1. ~~make camera setup with opencv~~
2. ~~train recognition with images and camera~~
3. ~~make backend api to transfer/handle data~~
4. ~~create a mongo db cluster and use through backend~~
5. ~~send details to backend from camera~~
6. make a frontend to get student tracks
7. send details to frontend from backend

# Intsall the Project

```sh
git clone https://github.com/NasheethAhmedA/student_tracking_system.git
```

# Installation for Camera

## Steps to folllow

```sh
python -m venv env
cd env/Scripts
activate
cd ../..
pip install dlib-19.24.99-cp312-cp312-win_amd64.whl  #[ only works for python 3.12 and you need to download the file ]
pip install requirements.txt
```

Then you can run the Detector.py or Train_face.py using ```python filename.py``` .