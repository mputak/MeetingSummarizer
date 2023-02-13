import openai
import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
import os


openai.api_key = "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"


class TextSummarization:
    def __init__(self, text, temp):

        self.model_engine = "text-davinci-003"
        self.temperature = temp
        self.chunks = self.break_up_file_to_chunks(text)
        self.prompt_responses = self.summarize(self.chunks)
        self.summary = self.consolidate(self.prompt_responses)

        self.write_to_file(self.summary)
        # self.prompt = f"Summarize the following text: {text}"
        # self.temperature = temp

        # Generate a summary
        # completion = openai.Completion.create(engine=self.model_engine, prompt=self.prompt,
        #                                       max_tokens=2000, n=1, stop=None, temperature=self.temperature)
        # summary = completion.choices[0].text

        # with open("summary.txt", "w") as file:
        #    file.write(summary)
        print("Done")

    def text_slicer(self, tokens, chunk_size, overlap_size):
        if len(tokens) <= chunk_size:
            yield tokens
        else:
            chunk = tokens[:chunk_size]
            yield chunk
            yield from self.text_slicer(tokens[chunk_size - overlap_size:], chunk_size, overlap_size)

    def break_up_file_to_chunks(self, text, chunk_size=2000, overlap_size=100):
        self.tokens = word_tokenize(text)
        return list(self.text_slicer(self.tokens, chunk_size, overlap_size))

    def convert_to_detokenized_text(self, tokenized_text):
        prompt_text = " ".join(tokenized_text)
        detokenized_text = prompt_text.replace(" 's", "'s")
        return detokenized_text

    def summarize(self, chunks):
        responses = []
        for i, chunk in enumerate(chunks):
            self.chunk_prompt_request = "Summarize this transcript: " + self.convert_to_detokenized_text(chunks[i])
            response = openai.Completion.create(engine=self.model_engine,
                                                prompt=self.chunk_prompt_request,
                                                max_tokens=500,
                                                n=1,
                                                stop=None,
                                                temperature=self.temperature,
                                                frequency_penalty=0,
                                                presence_penalty=0)
            responses.append(response.choices[0].text)
        return responses

    def consolidate(self, responses):
        self.consolidate_prompt_request = "Consoloidate these meeting summaries: " + str(responses)
        response = openai.Completion.create(engine=self.model_engine,
                                            prompt=self.consolidate_prompt_request,
                                            max_tokens=1000,
                                            n=1,
                                            stop=None,
                                            temperature=self.temperature,
                                            frequency_penalty=0,
                                            presence_penalty=0)
        return response.choices[0].text

    @staticmethod
    def write_to_file(summarized_text):
        with open("summary.txt", "w") as file:
            file.write(summarized_text)

TextSummarization("The speaker enjoys playing League of Legends,"
                  " typically as an attack damage carry with their girlfriend as support.", 0.2)
