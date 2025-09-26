#pip3 install SpeechRecognition pydub
import speech_recognition as sr
from heyprogram import Myprogram
from fichier import Fichier

class Texttospeech:
    def __init__(self,filename):
        self.filename=filename
        self.myprogram=Myprogram
    def script1(self):
        programs=self.myprogram(self.filename)
        programs.myargs(["./messcript/changetone.sh","./uploads/"+self.filename])
        print("debut du programme speech to text")
        try:
           if not Fichier("./uploads",self.filename.split(".")[0]+".wav").existe():
              programs.run()
        except Exception as e:
           print("error",e)
    def get_text(self,duration=30):
        # initialize the recognizer
        r = sr.Recognizer()

        #The below code is responsible for loading the audio file, and converting the speech into text using Google Speech Recognition:
        mytext=""
        # open the file
        with sr.AudioFile("./uploads/"+self.filename.split(".")[0]+".wav") as source:
                print("./uploads/"+self.filename.split(".")[0]+".wav")
                # listen for the data (load audio to memory)
                audio_data = r.record(source,duration=duration)
                # recognize (convert from speech to text)
                print("fromspeech to text")
                text = r.recognize_google(audio_data)
                mytext=(text)
        return mytext
    def get_text_hey(self,timeout=10,phrase_time_limit=3):
        # initialize the recognizer
        r = sr.Recognizer()

        #The below code is responsible for loading the audio file, and converting the speech into text using Google Speech Recognition:
        mytext=""
        # open the file
        with sr.AudioFile("./uploads/"+self.filename.split(".")[0]+".wav") as source:
                print("./uploads/"+self.filename.split(".")[0]+".wav")
                # listen for the data (load audio to memory)
                audio_data = r.record(source,timeout,phrase_time_limit)
                # recognize (convert from speech to text)
                print("fromspeech to text2")
                text = r.recognize_google(audio_data)
                mytext=(text)
        return mytext

