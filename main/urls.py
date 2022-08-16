from django.urls import path
from main.views import  *

app_name='main'

urlpatterns = [
    path('', index, name='index'),
    path('upload/', UploadPost.as_view(), name='upload'),
]