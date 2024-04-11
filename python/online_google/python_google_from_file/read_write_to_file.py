#import library
import speech_recognition as sr
import sys
import soundfile
import wave
import tempfile

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

data, samplerate = soundfile.read(sys.argv[1])
soundfile.write("/tmp/demo.wav", data, samplerate)

with sr.AudioFile("/tmp/demo.wav") as source:
    
    audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text, language = "it-IT")
        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')