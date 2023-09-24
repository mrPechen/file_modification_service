from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from file_handler.api.serializers.add_file_serializer import GetFilesSerializer
from file_handler.api.services.file_srevice import FileService
from file_handler.api import tasks


@api_view(['POST'])
def save_file(request):
    file = request.FILES['file']
    if 'image' in file.content_type or 'text' in file.content_type:
        data = FileService().save_file(file=file)
        serializer = GetFilesSerializer(data)
        content_type = file.content_type
        id = data.id
        tasks.files_processing.delay(file=str(file), id=id, type=content_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({'error': 'This file type is unsupported'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_files_list(request):
    data = FileService().get_all_files()
    serializer = GetFilesSerializer(data, many=True)
    return Response(serializer.data)
