# Student Tracking System

This a working prototype for a ML based student tracking/monitering system.
This can be used in any campus with security cameras for any corporation/institution.

## Benefits
- It can track and update everyones position at all time.
- It can be used to prevent any ill actions through ML models.
- It can be used for real time attendance/performance measurement.

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