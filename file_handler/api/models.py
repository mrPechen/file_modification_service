from django.db import models


class File(models.Model):
    file = models.FileField(verbose_name='File', upload_to='file_handler/api/files/original')
    uploaded_at = models.DateTimeField(verbose_name='Upload time', auto_now_add=True)
    processed = models.BooleanField(verbose_name='Processed', default=False)
