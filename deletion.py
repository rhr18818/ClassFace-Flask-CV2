from flask import Blueprint, render_template, request, jsonify, current_app
import shutil, os
from models import data_dir, known_encodings, known_names

deletion_bp = Blueprint('deletion', __name__)

@deletion_bp.route('/', methods=['GET'])
def list_regs():
    """
    Show a list of all person folders under data_faces_from_camera,
    parsed into ID, name, and folder name.
    """
    persons = []
    for folder in sorted(os.listdir(data_dir)):
        if not os.path.isdir(os.path.join(data_dir, folder)):
            continue
        parts = folder.split('_', 2)
        if len(parts) == 3 and parts[0] == 'person':
            idx, name = parts[1], parts[2]
            persons.append({'folder': folder, 'id': idx, 'name': name})
    return render_template('delete.html', persons=persons)

@deletion_bp.route('/remove', methods=['POST'])
def remove_reg():
    """
    AJAX endpoint: given a folder name, delete it from disk
    and also remove its encodings from memory.
    """
    data = request.get_json()
    folder = data.get('folder')
    folder_path = os.path.join(data_dir, folder)
    if not folder or not os.path.isdir(folder_path):
        return jsonify(status='error', message='Folder not found')

    # 1) Remove directory
    try:
        shutil.rmtree(folder_path)
    except Exception as e:
        return jsonify(status='error', message=f'Deletion failed: {e}')

    # 2) Purge from in-memory lists
    #    We cannot easily know which encodings belonged to which folder,
    #    so we simply clear the in-memory cache and force reload on next request.
    known_encodings.clear()
    known_names.clear()

    return jsonify(status='success', message=f'Registered student "{folder}" deleted successfully.')
