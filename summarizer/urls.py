# from django.urls import path
# from .views import summarize

# # app_name = 'summarizer'

# urlpatterns = [
#     path('api/summarize/', summarize, name='summarize'),
# ]

# from django.urls import path
# from .views import SummarizeAPIView  # Update the import to use the class-based view

# # app_name = 'summarizer'  # Uncomment if you are using namespacing

# urlpatterns = [
#     path('api/summarize/', SummarizeAPIView.as_view(), name='summarize'),  # Use as_view() for class-based view
# ]

# from django.urls import path
# from views.text_processing_view import TextProcessingView

# urlpatterns = [
#     path('api/process-text/', TextProcessingView.as_view(), name='process-text'),
# ]


from django.urls import path
from .views import TextProcessingView

urlpatterns = [
    path('api/v1/text-processing/', TextProcessingView.as_view(), name='text-processing'),
]


