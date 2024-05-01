from django.urls import path
from .views import ImageToBase64View

urlpatterns = [
    path('upload-img/', ImageToBase64View.as_view(), name='upload-img'),

]