# MeetingSummarizer
The purpose of the project is to give the user ability to fully focus on the meeting while recording it in the background. After the meeting ends, the program outputs a summarized version of the meeting in a .txt file.

- Note: The summary is abstractive, descriptive and accurate.


## How to use:

1. ```pip install -r requirements.txt``` in your working directory
2. export your OpenAI API Key through terminal: ```export OPEN_AI_API_KEY=YOUR_API_KEY```
3. make sure you have your microphone connected and run ```main.py```
4. record your meeting by pressing the **start** button
5. when done with the meeting, press the **summarize** button
6. Enjoy your summarized text in the directory under *summary.txt*

## FAQ:
- The project automatically opens the default microphone, but that can be changed by tweaking the given code in ```main.py```:

```python
        # Open the default microphone using PyAudio
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)
```

- The summarized text is slightly abstractive, which can be changed by adjusting the temperature setting in ```main.py```:

```python
    def summarize(self):
        self.text = SpeechToText().output
        self.temperature = 0.2
        TextSummarization(self.text, self.temperature)
```
Where ```self.temperature``` is a value between 0 and 1. The higher the value, the more abstract the summary will be and vice versa.