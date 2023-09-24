from django.urls import path
from file_handler.api import views


urlpatterns = [
    path('upload', views.save_file),
    path('files', views.get_files_list)
]
