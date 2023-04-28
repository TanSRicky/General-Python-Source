import re

class MessageList(object):

  def __init__ (self, folder):
    self._folder = folder
    self._messages = []

  def __getattr__ (self, attribute):
    return getattr (self._folder, attribute)

  def __iter__ (self):
    # NB You *must* collect a reference to the
    # Messages collection here; otherwise GetFirst/Next
    # resets every time.
    
    messages = self._folder.Items
    message = messages.GetFirst ()
    while message:
      yield message
      message = messages.GetNext ()
      
  def search(re,message):
    tmpList = []
    if  (re.search(pattern, message.subject) is not None or re.search(pattern, message.body) is not None):
     tmpList.append(message)
    return tmpList
       

    
    
