```python
import os
from flask import current_app
from werkzeug.utils import secure_filename

def save_file(file, date):
    filename = secure_filename(file.filename)
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], date, filename)
    file.save(file_path)
    return file_path

def get_files(date):
    folder_path = os.path.join(current_app.config['UPLOAD_FOLDER'], date)
    if os.path.exists(folder_path):
        return os.listdir(folder_path)
    return []

def get_file(date, filename):
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], date, filename)
    if os.path.exists(file_path):
        return file_path
    return None

def delete_file(date, filename):
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], date, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False
```