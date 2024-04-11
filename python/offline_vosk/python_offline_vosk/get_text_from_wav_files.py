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

# vosk-model-it-0.22
# vosk-model-small-en-us-0.15
model = Model(os.path.join(scriptLocation,sys.argv[3]))

jpExPartial = parse('$.partial')
jpExAll = parse('$.text')

textsByClass = {}
classAndExtraction = []

for filepath in glob.iglob(sys.argv[1]+"/**/*.wav"):    
    wavFileName = os.path.basename(filepath)
    clazz = os.path.basename(os.path.dirname(filepath))
    
    print(clazz+" : "+wavFileName)
    
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
            classAndExtraction.append(clazz+";"+value)
            #print(value)
    else:
        json_data = json.loads(rec.PartialResult())
        match = jpExPartial.find(json_data)
        value = match[0].value
        print(value)
        if value and value not in textsByClass[clazz]:
            textsByClass[clazz].append(value) 
            classAndExtraction.append(clazz+";"+value)
            #print(value)

#print(json.dumps(textsByClass, indent=4))
print("completed")

with open(sys.argv[2]+"/extracted_text.json", "w") as text_file:
    text_file.write(json.dumps(textsByClass))

csvString = "\n".join(classAndExtraction)  
with open(sys.argv[2]+"/extracted_text.csv", "w") as text_file:
    text_file.write(csvString)