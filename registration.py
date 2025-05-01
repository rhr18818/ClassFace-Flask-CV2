from flask import Blueprint, render_template, request, jsonify
import base64, cv2, os
import face_recognition
import numpy as np
from datetime import datetime
from models import known_encodings, known_names, load_known_faces, get_next_person_index, data_dir

registration_bp = Blueprint('registration', __name__)
load_known_faces()

@registration_bp.route('/', methods=['GET'])
def register_page():
    return render_template('register.html')

@registration_bp.route('/submit', methods=['POST'])
def register_submit():
    data = request.get_json()
    name = data.get('name','').strip().replace(' ','_')
    img_data = data.get('image','')
    if not name or not img_data:
        return jsonify(status='error', message='Missing name or image')
    header, enc = img_data.split(',',1)
    img_bytes = base64.b64decode(enc)
    arr = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encs = face_recognition.face_encodings(rgb)
    if len(encs) != 1:
        return jsonify(status='error', message='Ensure exactly one face')
    new_enc = encs[0]
    if any(face_recognition.compare_faces(known_encodings, new_enc)):
        return jsonify(status='error', message='Face already registered')
    idx = get_next_person_index()
    folder = f"person_{idx}_{name}"
    path = os.path.join(data_dir, folder)
    os.makedirs(path, exist_ok=True)
    fname = f"img_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    cv2.imwrite(os.path.join(path, fname), frame)
    known_encodings.append(new_enc)
    known_names.append(name)
    return jsonify(status='success', message=f'Registered {name}')