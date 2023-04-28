import win32com.client
from MessageIterator  import * 
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import text
import os 
import re 

def get_folders():
  constants = win32com.client.constants
  outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
  folders =  []
  messages = []  
  inbox = outlook.GetDefaultFolder(6)
  folders = []
  for i in range(100):
    try:
      # "6" refers to the index of a folder - in this case,
      folders.append(outlook.GetDefaultFolder(i))
    except Exception as e :
      print("Error at " + str(i) + ":" + str(e))
  return folders 

def get_emails():
  constants = win32com.client.constants
  outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
  folders =  []
  messages = []  
  inbox = outlook.GetDefaultFolder(6)
  all_msgs = MessageIterator(inbox) # Returns all COM references to emails.
  for m in all_msgs:
    messages.append(m)
  return messages

def main():
    searchString = 'BK'
    
    #create_engine('jdbcapi+pgjdbc://{}:{}@{}/{}'.format(username, password, "/lax.lax.ei:50012/,'BRDB'))
    for message in get_emails():
      print(message.subject)
     # print(em.body)
      attachments = message.Attachments

      for attachment in message.Attachments:
               # print(str(attachment))
          
                print(str(attachment.type))
                

                #attachment.SaveAsFile(os.path.join(path, str(attachment)))
                message.Unread = False


if __name__ == '__main__':
    main()