# Offline recognition with vosk

Vosk is an offline open source speech recognition toolkit

More details here

- https://github.com/alphacep/vosk-api
- https://alphacephei.com/vosk/

The following code will use vosk for speech recognition

## requirements

```
sudo apt install python3-pip
sudo apt-get install portaudio19-dev python3-pyaudio
```

python dependencies

```
pip3 install -r requirements.txt
```

## models

Download your model from here

https://alphacephei.com/vosk/models

unzip it at the root of this project

## run

Exec this passing the name of your downloaded model

```
python3 app.py "vosk-model-small-en-us-0.15"
```