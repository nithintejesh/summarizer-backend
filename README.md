# ConciseAI Backend

ConciseAI's backend is a Django-based REST API that serves the text summarization functionality of the application. It handles requests from the frontend and processes input using advanced natural language processing techniques.

## Features

- API endpoint for summarizing plain text, URLs, and PDF files.
- Uses TF-IDF ranking and NLP preprocessing to generate summaries.

## Technologies Used

- Django
- Django REST Framework
- Python
- Natural Language Processing

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/conciseai-backend.git
   cd conciseai-backend

2. Set up environment variables as needed (refer to .env.example)

3. Install the dependencies:
   ```bash
     pip install -r requirements.txt

4. Start the server:
   ```bash
     python manage.py runserver

5. The API will be available at `http://localhost:8000/api/v1/text-processing/`.

## API Endpoints

### Summarize Text

- **Endpoint:** `POST /api/summarize/`
- **Description:** Accepts plain text, URLs, or PDF files.
- **Returns:** A concise summary of the provided input.

## Frontend Repository

For the frontend application, visit the [ConciseAI Frontend Repository](https://github.com/nithintejesh/conciseai).

## Usage

- Use the API endpoint to summarize plain text, URLs, or PDF files.
- Refer to the API documentation for specific endpoint usage and parameters.

## Future Improvements

I plan to enhance the summarization capabilities of ConciseAI by transitioning from the current TF-IDF approach to more sophisticated and efficient methods. The goal is to provide users with even more accurate and relevant summaries, leveraging advanced techniques in natural language processing and machine learning.


## Contributing

Contributions and suggestions are always welcome! If you have ideas for improvements, new features, or find any issues, please feel free to reach out or submit a pull request. Your feedback is valuable in helping ConciseAI grow and improve.


## License

This project is licensed under the MIT License.

