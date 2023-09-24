from typing import Any

from file_handler.api.models import File


class FileRepository:
    def __init__(self):
        self.file_model = File

    def save_file(self, file: Any):
        result = self.file_model.objects.create(file=file)
        result.save()
        return result

    def change_processed_filed(self, id: int):
        file = self.file_model.objects.get(id=id)
        file.processed = True
        file.save()

    def get_file(self, id: int):
        result = self.file_model.objects.get(id=id)
        return result

    def get_all_files(self):
        result = self.file_model.objects.all()
        return result
