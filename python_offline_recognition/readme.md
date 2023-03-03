# Offline recognition

Reading about offline speech recognition I found:

- https://stackoverflow.com/a/73304153/3957754
- https://alphacephei.com/vosk/models

Not tried

- https://pypi.org/project/pocketsphinx/
- https://stackoverflow.com/questions/55895672/how-to-continuously-to-do-speech-recognition-while-outputting-the-recognized-wor

## Vosk

Vosk is an offline open source speech recognition toolkit

More details here

- https://github.com/alphacep/vosk-api
- https://alphacephei.com/vosk/

The following code will use vosk for speech recognition

## requirements

```
pip3 install vosk
pip3 install jsonpath_ng
pip3 install pyaudio
```

## vosk-model-small-en-us-0.15

**abite**

```
i've read the
i've been did
i've beat the
i've been the
i've read the
```

**defendere**

```
the offended
the thin dating
the friend did it
the finn did
the offended
```

**impetum**
```
in bit too
in bit too
in bit too
in bit too
embed don't
```

**remedium**
```
but i met you
the premier doom
re med doom
re med you
the made you
```

## vosk-model-small-it-0.22


**abite**

```
abiti
abiti
a vite
avi te
a te
```

**defendere**

```
difendere
difendere
difende
difendere
del fendi
```

**impetum**
```
in petto
in petto un
impetuoso
impeto un
impianto un
```

**remedium**
```
re medium
re medium
re medium
re medium
re medium
```