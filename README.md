# Facial Recognition Attendance System

This repository contains a Python-based Facial Recognition Attendance System. The system utilizes the LBPH algorithm for facial recognition along with the `haarcascade_frontalface_default.xml` file for face detection. It offers a user-friendly interface developed using the `tkinter` library and image processing functionalities through `Pillow` and `OpenCV`. Additionally, it integrates with MySQL database using `mysqlconnector` to store attendance records.

## Features

- Facial recognition for attendance tracking.
- User-friendly GUI for easy interaction.
- Automatic date and time stamping of attendance.
- MySQL integration for storing attendance records.
- Utilizes LBPH algorithm for face recognition.
- Face detection using haarcascade classifier.

## Requirements

Ensure you have the following libraries installed:

- `tkinter`
- `Pillow`
- `opencv-python`
- `numpy`
- `mysql-connector-python`

```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/Facial-Recognition-Attendance-System.git
```

2. Navigate to the project directory:

```bash
cd Facial-Recognition-Attendance-System
```

3. Run the `main.py` file:

```bash
python main.py
```

4. Follow the instructions on the GUI to take attendance.

## Note

Make sure to place the `haarcascade_frontalface_default.xml` file in the same directory as the `main.py` file for face detection to work properly.

## Contributors

- Atharv Porwal

Feel free to contribute by submitting bug fixes, feature requests, or pull requests.
