import pyaudio
import wave
import tkinter as tk
from tkinter import ttk
import threading
from textsummarization import TextSummarization
from speechtotext import SpeechToText


class AudioRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Summarizer 2000")

        # Create the main frame
        self.mainframe = ttk.Frame(self.root, padding="400 400 400 400")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.s = ttk.Style().configure("TFrame", background="#1c1c1c")

        # Create the label to display the current status
        self.status_label = ttk.Label(self.mainframe, text="Stopped",
                                      font=("Helvetica", 16), background="#1c1c1c", foreground="white")
        self.status_label.grid(column=0, row=0, columnspan=2, pady=50)

        # Create the "Record" button
        self.record_button = tk.Button(self.mainframe, text="Record", command=self.record,
                                       font=("Helvetica", 14), bg='#98FF98', fg='#000000', borderwidth=0)
        self.record_button.grid(column=0, row=1, sticky=tk.W, padx=50)

        # Create the "Stop" button
        self.stop_button = tk.Button(self.mainframe, text="Stop", command=self.stop,
                                     font=("Helvetica", 14), bg='#ff726f', fg='#000000', borderwidth=0)
        self.stop_button.grid(column=1, row=1, sticky=tk.W, padx=50)

        # Create the "Summarize" button
        self.summarize_button = tk.Button(self.mainframe, text="Summarize!",
                                          command=self.summarize, font=("Helvetica", 14))

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()

        # Set the audio parameters
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100

        # Create an empty list to store the recorded audio samples
        self.samples = []
        self.text = ""
        # Create a flag to track whether recording is in progress
        self.recording = False

    def record(self):
        # Update the status label to show that recording has started
        self.status_label.config(text="Recording")

        # Set the recording flag to True
        self.recording = True

        # Open the default microphone using PyAudio
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)

        # Start a new thread to continuously read audio samples from the microphone
        self.thread = threading.Thread(target=self.record_thread)
        self.thread.start()

    def record_thread(self):
        # Continuously read audio samples from the microphone while the recording flag is True
        while self.recording:
            data = self.stream.read(self.CHUNK)
            self.samples.append(data)

    def stop(self):
        # Update the status label to show that recording has stopped
        self.status_label.config(text="Stopped")
        self.summarize_button.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E), pady=50)
        # Set the recording flag to False
        self.recording = False

        # Close the microphone stream
        self.stream.stop_stream()
        self.stream.close()

        # Save the recorded audio to a .wav file
        wf = wave.open("recorded.wav", "wb")
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.samples))
        wf.close()

    def summarize(self):
        self.text = SpeechToText().output
        if self.text.count(" ") + 1 < 1500:
            TextSummarization(self.text)
        else:
            print("Too much words. The limit is 1500 words. Contact me if you would like to use full program features.")


# Create the root window
root = tk.Tk()
# Create the audio recorder GUI
audio_recorder = AudioRecorder(root)

# Run the main loop
root.mainloop()
