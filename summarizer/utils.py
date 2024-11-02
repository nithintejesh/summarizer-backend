import requests
import re
import bs4 as bs
import nltk
import math
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import fitz
from io import BytesIO

def preprocess_text(text):
    """Cleans the text by removing unwanted characters and lowercasing it."""
    text = re.sub(r'\[[0-9]*\]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

def extract_text_from_url(url):
    """Fetches web content from a given URL."""
    print(f"url is {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        parsed_article = bs.BeautifulSoup(response.text, 'html.parser')
        paragraphs = parsed_article.find_all('p')
        article_text = ''.join([p.text for p in paragraphs])
        return preprocess_text(article_text)
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"
    except Exception as e:
        return f"Error parsing the URL content: {e}"


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.
    :param pdf_file: Uploaded PDF file
    :return: Extracted text as a string
    """
    text = ""
    try:
        # Create an in-memory file object and open the PDF
        pdf_stream = BytesIO(pdf_file.read())
        print("PDF stream created successfully.")

        with fitz.open(stream=pdf_stream, filetype="pdf") as doc:
            print(f"Number of pages in PDF: {len(doc)}")
            for page in doc:
                text += page.get_text()
                print(f"Extracting text from page {page.number}.")

        return preprocess_text(text.strip())
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None


def get_text_input(data):
    """
    Retrieves and processes the text input based on data type.
    :param data: Dictionary with either 'text', 'url', or 'file' (PDF)
    :return: Extracted text as a string, or None if extraction fails
    """
    # print(data)
    if 'text' in data and data['text']:
        print(data['text'].strip())
        return data['text'].strip()
    elif 'url' in data and data['url']:
        print(data)
        return extract_text_from_url(data['url'])
    elif 'file' in data and data['file']:
        return extract_text_from_pdf(data['file'])
    return None

def tokenize_sentences(text):
    """Tokenizes text into sentences."""
    return sent_tokenize(text)

def tokenize_words(sentence, stop_words):
    """Tokenizes sentences into words and lemmatizes them."""
    words = word_tokenize(sentence)
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word.lower() not in stop_words]

def tf_idf_matrix(sentences, stop_words):
    """Calculates the TF-IDF matrix for the given sentences."""
    tf_matrix = {}
    for i, sent in enumerate(sentences):
        tf_table = {}
        words = tokenize_words(sent, stop_words)
        for word in words:
            tf_table[word] = tf_table.get(word, 0) + 1
        total_words = len(words)
        for word in tf_table:
            tf_table[word] = tf_table[word] / total_words
        tf_matrix[i] = tf_table

    idf_matrix = {}
    total_sentences = len(sentences)
    for i in range(total_sentences):
        for word in tf_matrix[i]:
            idf_matrix[word] = idf_matrix.get(word, 0) + 1
    for word in idf_matrix:
        idf_matrix[word] = math.log(total_sentences / float(idf_matrix[word]))

    tf_idf = {i: {word: tf_matrix[i][word] * idf_matrix[word] for word in tf_matrix[i]} for i in tf_matrix}

    return tf_idf

def score_sentences(sentences, tf_idf):
    """Scores sentences based on their TF-IDF values."""
    sentence_scores = {}
    for i, sent in enumerate(sentences):
        score = sum(tf_idf[i].values())
        sentence_scores[sent] = score / len(sent.split())
    return sentence_scores

def generate_summary(sentences, sentence_scores, threshold):
    """Generates a summary based on sentence scores."""
    summary = " ".join([sent for sent in sentences if sentence_scores.get(sent, 0) >= threshold])
    return summary

def summarize(data):
    """
    Processes input data (text, URL, or file) and generates a summary.
    :param data: Dictionary containing 'text', 'url', or 'file' key with the respective content
    :return: Summary of the extracted content
    """
    text = get_text_input(data)
    if not text:
        return "Failed to extract text. Please provide valid input."

    sentences = tokenize_sentences(text)
    stop_words = set(stopwords.words("english"))
    tf_idf = tf_idf_matrix(sentences, stop_words)
    sentence_scores = score_sentences(sentences, tf_idf)
    threshold = sum(sentence_scores.values()) / len(sentence_scores)
    summary = generate_summary(sentences, sentence_scores, 1.3 * threshold)

    return summary
