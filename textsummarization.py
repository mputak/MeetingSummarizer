import openai
import config


openai.api_key = config.API_KEY


class TextSummarization:
    def __init__(self, text):

        self.model_engine = "text-davinci-003"
        self.prompt = f"Please summarize the following text: {text}"

        # Generate a summary
        completion = openai.Completion.create(engine=self.model_engine, prompt=self.prompt,
                                              max_tokens=1024, n=1, stop=None, temperature=0.2)
        summary = completion.choices[0].text

        with open("summary.txt", "w") as file:
            file.write(summary)
