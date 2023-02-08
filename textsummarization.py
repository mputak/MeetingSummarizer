import openai
import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
import os


openai.api_key = "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"


class TextSummarization:
    def __init__(self, text, temp):

        self.model_engine = "text-davinci-003"
        self.token_count = self.token_counter(text)
        # self.prompt = f"Summarize the following text: {text}"
        # self.temperature = temp

        # Generate a summary
        # completion = openai.Completion.create(engine=self.model_engine, prompt=self.prompt,
        #                                       max_tokens=2000, n=1, stop=None, temperature=self.temperature)
        # summary = completion.choices[0].text

        # with open("summary.txt", "w") as file:
        #    file.write(summary)
        print("Done")

# Change file to text, remove open...
    def token_counter(self, file):
        with open(file, "r") as f:
            text = f.read()
        self.tokens = word_tokenize(text)
        print(len(self.tokens))
        return len(self.tokens)

    def text_slicer(self, text, chunk_size=2000, overlap_size=100):


TextSummarization("summary.txt", 0.2)
