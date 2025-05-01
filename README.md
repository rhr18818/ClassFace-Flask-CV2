# 🎓 Face Recognition-Based Student Registration & Attendance System

> _“Roll call, but make it future-proof!”_

Welcome to our goofy (yet highly practical) face-powered attendance app. This Flask-based marvel replaces tedious paper sign-ins with sweet, sweet automation—and it even remembers your name (so you don’t have to say it 50 times).

---

## 🚀 Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Prerequisites](#prerequisites)  
5. [Installation & Setup](#installation--setup)  
6. [How to Use](#how-to-use)  
7. [Directory Structure](#directory-structure)  
8. [Troubleshooting](#troubleshooting)  
9. [Future Improvements](#future-improvements)  
10. [Contributing](#contributing)  
  

---

## 📝 Project Overview

Traditional classroom attendance is _so_ 20th century: paper sheets, proxy buddies, chalk-dust fingers… yikes!  
Our app brings attendance into the 21st century using **face recognition**:

1. **Register** each student with a live webcam snap  
2. **Select** your course from a friendly dropdown  
3. **“Mark Attendance”** by showing your face to the camera  
4. **Manage** (and delete) registrations when your cousin graduates  

All with a snazzy Bootstrap UI, because you deserve something prettier than plain HTML. 😉

---

## ✨ Features

- **Seamless Registration**  
  - Live video preview, enter your Student ID & Name, click “Capture & Register.”  
- **Effortless Attendance**  
  - Pre-populated course dropdown (farewell, typos!)  
  - Real-time face matching & automatic logging.  
- **Attendance Records**  
  - SQLite database for today’s sessions  
  - “Show Attendance” page with a clean table view.  
- **Admin Tools**  
  - Delete outdated registrations in a click (RIP old grads).  
- **Resource-Friendly**  
  - Boxes draw only on demand, vanish after 2 seconds. No resource hogging here!

---

## 🛠 Tech Stack

- **Backend:** Python 3.x + Flask  
- **Face Magic:** `face_recognition` (built on dlib) + OpenCV  
- **Frontend:** HTML5, Bootstrap 5, vanilla JavaScript  
- **Storage:**  
  - Face images in `data/data_faces_from_camera/person_<N>_<name>/`  
  - SQLite for attendance logs  

---

## 🔧 Prerequisites

- Python **3.8+**  
- Modern browser with webcam support  
- (Optional, Windows users) CMake + pre-built dlib if face-recognition install won’t compile  

---

## 📥 Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-org/face-attendance.git
   cd face-attendance
   ```

2. **Create a virtual environment** (recommended!)  
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux / macOS
   venv\Scripts\activate     # Windows PowerShell
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**  
   The first run of `app.py` auto-creates `attendance.db` with the right table.

5. **Run the app**  
   ```bash
   python app.py
   ```  
   By default, it listens on `http://0.0.0.0:5000/`

6. **Open your browser**  
   Navigate to `http://localhost:5000` and bask in the glory of face-powered attendance.


## 🎁 Bonus Tips

> **Pro Tip:** If you are unable to download dlib from the terminal, use the manual approach:

Git Link for dlib file: https://github.com/z-mahmud22/Dlib_Windows_Python3.x/tree/main

---

## 🎬 How to Use

1. **Home Page**  
   - Choose **Register**, **Take Attendance**, or **Manage Registrations** from the navbar.

2. **Register New Student**  
   - Enter **ID** and **Name**.  
   - Align your face in the camera box.  
   - Click **Capture & Register**.  
   - If your face is already registered, the app politely declines.

3. **Take Attendance**  
   - Select a course (no more manual typing!).  
   - Align face, click **Capture & Mark Attendance**.  
   - Success popup shows who got marked—no awkward roll calls!

4. **Show Attendance**  
   - Click **Show Attendance** to see today’s logged students in a clean table.

5. **Manage Registrations**  
   - Click the trash button next to any old student to delete their registration (and their face images).  

---

## 📁 Directory Structure

```
flask_app/
├── app.py
├── models.py
├── registration.py
├── attendance.py
├── deletion.py
├── requirements.txt
├── attendance.db
├── data/
│   └── data_faces_from_camera/
│       └── person_1_Ratul/…
└── templates/
    ├── base.html
    ├── index.html
    ├── register.html
    ├── take_attendance.html
    ├── show_attendance.html
    └── delete.html
```

---

## 🐞 Troubleshooting

- **“No webcam detected”**  
  - Ensure your browser has camera permission.  
  - Check `navigator.mediaDevices` support.

- **`face_recognition` install errors on Windows**  
  - Install [CMake](https://cmake.org/) and use pre-built dlib wheels.

- **Duplicate face registrations**  
  - Good! The system detected you already exist. Try deleting first if it’s a test user.

- **Black bars around video**  
  - Our CSS uses `object-fit: cover`; if you still see bars, tweak the inline styles.

---

## 🛣 Future Improvements

- Export attendance as **CSV** / Excel  
- **Email notifications** (Prof, your students are missing!)  
- **Analytics dashboard** (Who sleeps most in class?)  
- **Mobile-friendly UI** for tablets & phones  

---

## 🤝 Contributing

1. Fork it  
2. Create your feature branch: `git checkout -b feature/amazing`  
3. Commit your changes: `git commit -m 'Add amazing feature'`  
4. Push to the branch: `git push origin feature/amazing`  
5. Open a Pull Request—bonus points for memes in your description.



> “Technology may fail, but attendance never does.”  
> – Your friendly neighborhood Computer Science lab team 😎  
