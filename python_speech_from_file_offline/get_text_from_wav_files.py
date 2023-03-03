import sys
import wave
import tempfile
from jsonpath_ng import jsonpath, parse
import json
import sys
from vosk import Model, KaldiRecognizer
import glob
import os
import soundfile

scriptLocation = os.path.dirname(os.path.realpath(__file__))

model = Model(os.path.join(scriptLocation,"vosk-model-small-it-0.22"))

jpExPartial = parse('$.partial')
jpExAll = parse('$.text')

textsByClass = {}

for filepath in glob.iglob(sys.argv[1]+"/**/*.wav"):
    print(filepath)
    wavFileName = os.path.basename(filepath)
    clazz = os.path.basename(os.path.dirname(filepath))
    if clazz not in textsByClass:
      textsByClass[clazz] = []

    
    try:
      wf = wave.open(filepath, "rb")
    except Exception as e:
      if 'RIFF' in e.args[0]:
        print(e.args[0]+"... Re-read...")
        data, samplerate = soundfile.read(filepath)
        soundfile.write("/tmp/"+wavFileName, data, samplerate)
        wf = wave.open("/tmp/"+wavFileName, "rb")
      else:
        print('Err not supported:'+e.args[0])


    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        continue
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    data = wf.readframes(wf.getnframes())
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        json_data = json.loads(rec.Result())
        match = jpExAll.find(json_data)
        value = match[0].value
        print(value)
        if value and value not in textsByClass[clazz]:
            textsByClass[clazz].append(value)
            #print(value)
    else:
        json_data = json.loads(rec.PartialResult())
        match = jpExPartial.find(json_data)
        value = match[0].value
        print(value)
        if value and value not in textsByClass[clazz]:
            textsByClass[clazz].append(value) 
            #print(value)

#print(json.dumps(textsByClass, indent=4))
print("completed")

with open(sys.argv[1]+"_extracted_text.json", "w") as text_file:
    text_file.write(json.dumps(textsByClass))