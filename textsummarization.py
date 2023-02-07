import openai
import os


openai.api_key = "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"


class TextSummarization:
    def __init__(self, text, temp):

        self.model_engine = "text-davinci-003"
        self.prompt = f"Summarize the following text: {text}"
        self.temperature = temp

        # Generate a summary
        completion = openai.Completion.create(engine=self.model_engine, prompt=self.prompt,
                                              max_tokens=2000, n=1, stop=None, temperature=self.temperature)
        summary = completion.choices[0].text

        with open("summary.txt", "w") as file:
            file.write(summary)
        print("Done")
