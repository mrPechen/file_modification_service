from typing import Any

from file_handler.api.repository.file_repository import FileRepository
import cv2
import shutil


class FileService:
    def __init__(self):
        self.file_repository = FileRepository()
        self.processed_path = 'file_handler/api/files/processed/processed'
        self.new_text = 'Append a new line'

    def save_file(self, file):
        return self.file_repository.save_file(file=file)

    def img_file_processing(self, file: Any, id: int):
        filename = str(self.get_file_path(id=id))
        img_rgb = cv2.imread(filename)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        self.file_repository.change_processed_filed(id=id)
        return cv2.imwrite(f'{self.processed_path}_id_{id}_{file}', img_gray)

    def txt_file_processing(self, file: Any, id: int):
        original_path = str(self.get_file_path(id=id))
        processed_path = f'{self.processed_path}_id_{id}_{file}'
        print(original_path)
        shutil.copyfile(original_path, processed_path)
        with open(original_path, 'r') as original: data = original.read()
        with open(processed_path, 'w') as processed: processed.write(data + f'\n{self.new_text}')
        original.close()
        processed.close()
        self.file_repository.change_processed_filed(id=id)

    def processing_files(self, file: Any, id: int, type: str):
        if 'image' in type:
            return self.img_file_processing(file=file, id=id)
        if 'text' in type:
            return self.txt_file_processing(file=file, id=id)

    def get_file_path(self, id: int):
        result = self.file_repository.get_file(id=id).file
        return result

    def get_all_files(self):
        return self.file_repository.get_all_files()
