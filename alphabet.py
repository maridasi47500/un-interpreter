from espeakng import ESpeakNG
class Ipa():
    def __init__(self,text="Hello World",pitch=32,speed=150,voice="english-us"):
        #voice = erman
        self.esng=ESpeakNG()
        self.esng.pitch=pitch
        self.esng.speed=speed
        self.esng.voice=voice
        self.text=text
    def to_ipa(self,ipa=2)
        ipa1=self.esng.g2p(self.text,ipa=ipa)
        return ipa1
