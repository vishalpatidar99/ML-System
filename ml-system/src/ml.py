import torch
import torch.nn as nn
import re
import langid
from iso639 import languages


# Define constants
MAX_LENGTH = 100  # Maximum length of input string
NUM_LANGUAGES = 100  # Maximum number of languages to consider


def job_executor_handler(data):
    return str(detect_languages(data))


# Convert text to tensor
def text_to_tensor(text):
    tensor = torch.zeros(MAX_LENGTH, dtype=torch.long)
    for i, char in enumerate(text):
        tensor[i] = ord(char)  # Convert character to ASCII code
    return tensor


# Define the RNN model
class LanguageDetector(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LanguageDetector, self).__init__()
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.rnn = nn.RNN(hidden_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, input):
        embedded = self.embedding(input)
        output, _ = self.rnn(embedded.view(len(input), 1, -1))
        output = self.fc(output[-1])
        return output
    

# Function to detect languages in input text
def detect_languages(text):
    def tokenize(text):
        return re.findall(r'\b\w+\b', text)

    def detect_language_percentage(text):
        words = tokenize(text)
        detected_languages = [langid.classify(word)[0] for word in words]
        language_counts = {lang: detected_languages.count(lang) for lang in set(detected_languages)}
        total_words = sum(language_counts.values())
        language_percentages = {lang: (count / total_words) * 100 for lang, count in language_counts.items()}
        return language_percentages

    language_percentages = detect_language_percentage(text)
    language_codes = list(language_percentages.keys())
    language_names = fetch_language_names(language_codes)

    return {languages.get(alpha2=lang).name: f"{percentage:.2f}%" for lang, percentage in language_percentages.items()}


# Function to fetch language names dynamically
def fetch_language_names(language_codes):
    language_names = {}
    for code in language_codes:
        language_names[code] = languages.get(alpha2=code).name
    return language_names

