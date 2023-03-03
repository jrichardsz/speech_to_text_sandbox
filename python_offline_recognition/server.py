from vosk import Model, KaldiRecognizer
import pyaudio
from jsonpath_ng import jsonpath, parse
import json
import sys

model = Model(r"vosk-model-small-it-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

jsonpath_expression = parse('$.text')

while True:
    data = stream.read(4096)
    
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        json_data = json.loads(text)
        match = jsonpath_expression.find(json_data)
        print(match[0].value)