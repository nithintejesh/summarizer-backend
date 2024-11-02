from django.urls import path
from .views import TextProcessingView

urlpatterns = [
    path('api/v1/text-processing/', TextProcessingView.as_view(), name='text-processing'),
]


