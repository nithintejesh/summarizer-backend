from django.apps import AppConfig
import nltk
import  os

class SummarizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'summarizer'

    def ready(self):
        # Ensure necessary NLTK data is downloaded
        self.ensure_nltk_data()

    def ensure_nltk_data(self):
        nltk_data_path = os.path.join(nltk.data.path[0], 'corpora')
        required_resources = ['punkt', 'wordnet', 'stopwords']

        for resource in required_resources:
            resource_path = os.path.join(nltk_data_path, resource)
            if not os.path.exists(resource_path):
                nltk.download(resource)
                print(f"Downloaded {resource} corpus.")
            else:
                print(f"{resource} corpus already present.")