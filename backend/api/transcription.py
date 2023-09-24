```python
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from .file_management import save_file, get_file_path
from .celery_tasks import transcribe_audio
import os

transcription_bp = Blueprint('transcription', __name__)

@transcription_bp.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    save_file(file, filename)

    file_path = get_file_path(filename)
    task = transcribe_audio.delay(file_path)

    return jsonify({'message': 'Transcription started', 'task_id': str(task.id)}), 202

@transcription_bp.route('/transcribe/<task_id>', methods=['GET'])
def get_transcription_status(task_id):
    task = transcribe_audio.AsyncResult(task_id)

    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'status': str(task.info)
        }
    else:
        response = {
            'state': task.state,
            'status': str(task.info)
        }

    return jsonify(response)
```