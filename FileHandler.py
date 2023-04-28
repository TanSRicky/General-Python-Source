import os 
import re 

class FileHandler():



    def __init__ (self):
        self._ext = "None"
        self._size = 'Master'
        self._token_list = ['.pdf',]


    def __getattr__ (self, attribute):
        return getattr (self._ext, attribute)
