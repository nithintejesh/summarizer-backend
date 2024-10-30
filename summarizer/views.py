# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .utils import fetch_web_content, summarize_article
# # import logging
# import re
# import json


# class SummarizeAPIView(APIView):
#     def post(self, request):
#         print("Post method reached")
#         print(request.body)  # Print raw body to verify incoming data
#         try:
#             url_data = json.loads(request.body)
#             print(url_data)
#             url = url_data.get("url", "").strip()  # Accessing URL from the parsed JSON
#         except json.JSONDecodeError:
#             return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)

#         print(f"url is: {url}")
#         if not url:
#             return Response({"error": "URL is required."}, status=status.HTTP_400_BAD_REQUEST)

#         article_text = fetch_web_content(url)
#         if article_text.startswith("Error"):
#             return Response({"error": article_text}, status=status.HTTP_400_BAD_REQUEST)

#         summary = summarize_article(article_text)
#         return Response({"summary": summary}, status=status.HTTP_200_OK)




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import json
# from .utils import get_text_input, summarize

# class TextProcessingView(APIView):
#     def post(self, request, format=None):
#         try:
#             data = json.loads(request.body)
#             print("Received data:", data)
#         except json.JSONDecodeError:
#             return Response({"error": "Invalid JSON format."}, status=status.HTTP_400_BAD_REQUEST)

#         print(f"data: {data}")
#         extracted_text = get_text_input(data)

#         # Validate that text extraction was successful
#         # if not extracted_text:
#         #     return Response({"error": "Failed to extract text. Please provide valid input."}, status=status.HTTP_400_BAD_REQUEST)

#         # Core processing on the extracted text
#         summary = summarize(extracted_text)
#         return Response({"summary": summary}, status=status.HTTP_200_OK)






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .utils import get_text_input, summarize

class TextProcessingView(APIView):
    def post(self, request, format=None):
        try:
            # Load the JSON data from the request body
            data = json.loads(request.body)
            print("Received data:", data)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format."}, status=status.HTTP_400_BAD_REQUEST)

        print(f"data: {data}")
        
        # Extract text based on the provided input type
        extracted_text = get_text_input(data)

        # Validate that text extraction was successful
        if not extracted_text:
            return Response({"error": "Failed to extract text. Please provide valid input."}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare the data for summarization
        summarization_input = {
            'text': extracted_text if isinstance(extracted_text, str) else '',
            'url': data.get('url', ''),
            'file': data.get('file', None)
        }

        # Core processing on the extracted text
        summary = summarize(summarization_input)

        return Response({"summary": summary}, status=status.HTTP_200_OK)








# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser
# from .utils import get_text_input
# from .utils import summarize  # Assuming summarize_article is your common text processing function

# class TextProcessingView(APIView):
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         # Use the unified text extraction utility
#         extracted_text = get_text_input({
#             "text": request.data.get('text'),
#             "url": request.data.get('url'),
#             "file": request.FILES.get('file')
#         })

#         # Validate that text extraction was successful
#         if not extracted_text:
#             return Response({"error": "Failed to extract text. Please provide valid input."}, status=status.HTTP_400_BAD_REQUEST)

#         # Core processing on the extracted text
#         summary = summarize_article=(extracted_text)
#         return Response({"summary": summary}, status=status.HTTP_200_OK)




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .utils import get_text_input, summarize
# import json

# class TextProcessingView(APIView):
#     def post(self, request, format=None):
#         try:
#             # Parse JSON data from the request body
#             data = json.loads(request.body)
#             # url = data.get("url", "").strip()
#             print(data)
#         except json.JSONDecodeError:
#             return Response({"error": "Invalid JSON format."}, status=status.HTTP_400_BAD_REQUEST)

#         extracted_text = get_text_input({
#             "text": data.get('text'),
#             "url": data.get('url'),
#             "file": request.FILES.get('file')
#         })
#         # Validate that text extraction was successful
#         if not extracted_text:
#             return Response({"error": "Failed to extract text. Please provide valid input."}, status=status.HTTP_400_BAD_REQUEST)

#         # Core processing on the extracted text
#         summary = summarize(extracted_text)
#         return Response({"summary": summary}, status=status.HTTP_200_OK)

# class TextProcessingView(APIView):
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         extracted_text = get_text_input({
#             "text": request.data.get('text'),
#             "url": request.data.get('url'),
#             "file": request.FILES.get('file')
#         })

#         if not extracted_text or "Error" in extracted_text:
#             return Response({"error": "Failed to extract text. Please provide valid input."}, status=status.HTTP_400_BAD_REQUEST)

#         # Process the text and generate summary
#         summary = summarize({"text": extracted_text})
#         return Response({"summary": summary}, status=status.HTTP_200_OK)









# class SummarizeAPIView(APIView):
#     def post(self, request):
#         print("Post method reached") 
#         print(request.body)
#         # url = request.data.get("url")
#         print(request.data)
#         url = request.data.get("url", "").strip()  
#         print(f"url is: {url}")
#         if not url:
#             return Response({"error": "URL is required."}, status=status.HTTP_400_BAD_REQUEST)

#         article_text = fetch_web_content(url)
#         if article_text.startswith("Error"):
#             return Response({"error": article_text}, status=status.HTTP_400_BAD_REQUEST)

#         summary = summarize_article(article_text)
#         return Response({"summary": summary}, status=status.HTTP_200_OK)


# class SummarizeAPIView(APIView):

#     def post(self, request):
#         """Handles POST requests to summarize an article."""
#         url = request.data.get('url')
#         if not url:
#             return Response({"error": "URL is required."}, status=status.HTTP_400_BAD_REQUEST)

#         summary = summarize_article(url)
#         if summary.startswith("Error"):
#             return Response({"error": summary}, status=status.HTTP_400_BAD_REQUEST)

#         return Response({"summary": summary}, status=status.HTTP_200_OK)
