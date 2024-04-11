https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426
https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages

## requirements

```
pip3 install numpy
pip3 install soundfile
```

## disadvantages

google speech is required

## from file

If you wav is "standard"

```
python3  direct_sound_file.py /.../defendere.wav 
```

**output**

```
result2:
{   'alternative': [   {'confidence': 0.92336094, 'transcript': 'defendere'},
                       {'transcript': 'Defender'},
                       {'transcript': 'difendere'}],
    'final': True}
Converting audio transcripts into text ...
defendere
```

## non standard wav

If you have these errors

```
wave.Error: file does not start with RIFF id
Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format"
ValueError: Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format
```

You should need to read the file and write to another file before the detection. Also you could need ffmpeg to convert the wav to mp3 and mp3 to wav. That worked for me


Audio file must be WAV format mono PCM.
ffmpeg to convert

## from wav

python3 get_text_from_wav_files.py /home/computer/This/sentences/latin/oversampled /home/computer/This/sentences/latin