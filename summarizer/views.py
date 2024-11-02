from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from .utils import get_text_input, summarize

class TextProcessingView(APIView):
    # Allow parsing of both multipart form data and JSON
    parser_classes = [MultiPartParser, JSONParser]

    def post(self, request, format=None):
        # Use request.data to handle both JSON and file data
        data = request.data

        # Print received data for debugging
        print("Received data:", data)

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