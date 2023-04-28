

class OutlookConnector:

    def __init__ (self):
            import win32com.client
            self._outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
            self._messages = []
            self._folders = []
            self._current = MessageList(outlook.GetDefaultFolder(6)) 
            
    def __getattr__ (self, attribute):
        return getattr (self, attribute)

    def set_folders():
        folders = outlook.GetDefaultFolder(6).Folders

    def set_messages():
        outlook = Connector.connect_outlook()

    def get_folders():
        for f in  folders:
            print (f.name)
    
    def get_messages():
        for f in  folders:
            print (f.name)