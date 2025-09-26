import os
import glob
from sys import argv
from pydub import AudioSegment
import os
import glob
from pydub import AudioSegment
def strip_end(text, suffix):
    if suffix and text.endswith(suffix):
        return text[:-(len(suffix) + 1)]
    return text
class Socialmedia():

    def __init__(self,myname="hey.m4a"):
        self.myname=myname
        print("hello123")
    def ok(self):
        INPUT_FORMAT = 'm4a'
        OUTPUT_FORMAT = 'mp3'

        # find all files that end with m4a
        
        print('----------------------------------------\n')
        
        # loop converting files and showing progress of each

        
        
        print('----------------------------------------\n')
        
        # loop converting files and showing progress of each
        myname=self.myname
        print('name', myname)
        file_name = "./uploads/"+strip_end(myname,INPUT_FORMAT)
        print('Converting', file_name)
        
        destination = file_name+"."+OUTPUT_FORMAT
        print('destination', destination)
        
        output = AudioSegment.from_file(file_name+"."+INPUT_FORMAT, format=INPUT_FORMAT)
        output.export(destination, format=OUTPUT_FORMAT)
        
        print('Done\n')
        
        # display completion and where files are located
        print('Converting', file_name)
        
        
        
        print('All files have been converted and can be found in')
