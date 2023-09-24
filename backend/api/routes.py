```python
from flask import Blueprint, request, jsonify
from .auth import token_required
from .file_management import save_file, get_file, delete_file, list_files
from .transcription import transcribe_file
from .celery_tasks import transcribe_task

api = Blueprint('api', __name__)

@api.route('/upload', methods=['POST'])
@token_required
def upload_file():
    file = request.files['file']
    date = request.form['date']
    save_file(file, date)
    return jsonify({'message': 'File uploaded successfully'}), 200

@api.route('/files', methods=['GET'])
@token_required
def get_files():
    date = request.args.get('date')
    files = list_files(date)
    return jsonify({'files': files}), 200

@api.route('/file', methods=['GET', 'DELETE'])
@token_required
def handle_file():
    date = request.args.get('date')
    filename = request.args.get('filename')
    if request.method == 'GET':
        file = get_file(date, filename)
        return jsonify({'file': file}), 200
    elif request.method == 'DELETE':
        delete_file(date, filename)
        return jsonify({'message': 'File deleted successfully'}), 200

@api.route('/transcribe', methods=['POST'])
@token_required
def transcribe():
    date = request.form['date']
    filename = request.form['filename']
    transcribe_task.delay(date, filename)
    return jsonify({'message': 'Transcription started'}), 200
```