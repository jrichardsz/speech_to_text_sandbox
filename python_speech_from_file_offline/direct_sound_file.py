import sys
import wave
import tempfile
from jsonpath_ng import jsonpath, parse
import json
import sys
from vosk import Model, KaldiRecognizer
import glob

model = Model(r"vosk-model-small-it-0.22")

jpExPartial = parse('$.partial')
jpExAll = parse('$.text')


for filepath in glob.iglob(sys.argv[1]+"/**/*.wav"):
    print(filepath)
    wf = wave.open(filepath, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    data = wf.readframes(wf.getnframes())
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        json_data = json.loads(rec.Result())
        match = jpExAll.find(json_data)
        print(match[0].value)          
    else:
        json_data = json.loads(rec.PartialResult())
        match = jpExPartial.find(json_data)
        print(match[0].value)        