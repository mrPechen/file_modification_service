from rest_framework import serializers
from file_handler.api.models import File


class GetFilesSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField()

    def get_filename(self, obj):
        name = str(obj.file)
        return name

    class Meta:
        model = File
        fields = ['id', 'filename', 'processed']
