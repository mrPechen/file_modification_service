from typing import Any

from file_handler.api.celery_dir.celery import app
from file_handler.api.services.file_srevice import FileService


@app.task
def files_processing(file: Any, id: int, type: str):
    FileService().processing_files(file=file, id=id, type=type)
