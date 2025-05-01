import os
import sqlite3
import face_recognition

base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, 'data', 'data_faces_from_camera')
if not os.path.exists(data_dir): os.makedirs(data_dir)

# SQLite setup
db_path = os.path.join(base_dir, 'attendance.db')
conn = sqlite3.connect(db_path, check_same_thread=False)
c = conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    course_code TEXT,
    date TEXT,
    person_name TEXT
)''')
conn.commit()

# Known faces cache
known_encodings = []
known_names = []

def load_known_faces():
    global known_encodings, known_names
    for person in os.listdir(data_dir):
        folder = os.path.join(data_dir, person)
        if os.path.isdir(folder):
            for img in os.listdir(folder):
                path = os.path.join(folder, img)
                encs = face_recognition.face_encodings(
                    face_recognition.load_image_file(path)
                )
                if encs:
                    known_encodings.append(encs[0])
                    # extract name from folder: person_<idx>_<name>
                    parts = person.split('_')[2:]
                    known_names.append('_'.join(parts) if parts else person)

def get_next_person_index():
    existing = [d for d in os.listdir(data_dir) if d.startswith('person_')]
    nums = [int(d.split('_')[1]) for d in existing if d.split('_')[1].isdigit()]
    return max(nums) + 1 if nums else 1
