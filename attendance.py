from flask import Blueprint, render_template, request, jsonify
import base64, cv2
import face_recognition
import numpy as np
from datetime import datetime
from models import known_encodings, known_names, conn, data_dir

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/take', methods=['GET'])
def take_page():
    return render_template('take_attendance.html')

@attendance_bp.route('/mark', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    course = data.get('course','').strip()
    code = data.get('code','').strip()
    img_data = data.get('image','')
    if not course or not code or not img_data:
        return jsonify(status='error',message='Missing data')
    header, enc = img_data.split(',',1)
    frame = cv2.imdecode(np.frombuffer(base64.b64decode(enc), np.uint8), cv2.IMREAD_COLOR)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    locs = face_recognition.face_locations(rgb)
    encs = face_recognition.face_encodings(rgb, locs)
    names = []
    for e in encs:
        m = face_recognition.compare_faces(known_encodings, e)
        name = known_names[m.index(True)] if True in m else 'Unknown'
        names.append(name)
        date_str = datetime.now().strftime('%Y-%m-%d')
        conn.execute('INSERT INTO attendance(course_name,course_code,date,person_name) VALUES(?,?,?,?)',
                     (course, code, date_str, name))
    conn.commit()
    return jsonify(status='success', message='Marked: ' + ', '.join(names))

@attendance_bp.route('/show', methods=['GET'])
def show_attendance():
    c = conn.cursor()
    today = datetime.now().strftime('%Y-%m-%d')
    c.execute('SELECT course_name, course_code, date, person_name FROM attendance WHERE date=?', (today,))
    rows = c.fetchall()
    records = [{'course': r[0], 'code': r[1], 'date': r[2], 'name': r[3]} for r in rows]
    return render_template('show_attendance.html', records=records)