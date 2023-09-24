```python
from celery import Celery
from .config import Config
from .transcription import transcribe_audio
from .file_management import delete_file

celery = Celery(__name__)
celery.config_from_object(Config)

@celery.task
def transcribe_audio_task(file_path):
    return transcribe_audio(file_path)

@celery.task
def delete_file_task(file_path):
    return delete_file(file_path)
```