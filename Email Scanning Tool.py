from MessageList  import * 
from Connector import *

def main():
    outlook = Connector.connect_outlook()
    folders =  []
    pattern = r'(BK|bk){1}[0-9]{8}'
    msg_list =  MessageList(outlook.GetDefaultFolder(6)) 
    for message in msg_list:
      if  (re.search(pattern, message.subject) is not None or re.search(pattern, message.body) is not None):
        print(message.subject)
      attachments = message.Attachments
      message.Unread = True
      for attachment in message.Attachments:
                print(str(attachment))
                message.Unread = False



if __name__ == '__main__':
    main()