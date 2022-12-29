import speech_recognition as sr


class SpeechToText:
    def __init__(self):

        self.r = sr.Recognizer()
        self.audio_file = sr.AudioFile("recorded.wav")
        with self.audio_file as source:
            self.r.adjust_for_ambient_noise(source)
            self.audio = self.r.record(source)

        self.output = self.r.recognize_google(self.audio)
