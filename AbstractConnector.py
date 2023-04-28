from abc import ABC,abstractmethod 

class Connector:
    def __init__ (self,db,server):
        self._db = db
        self._server = server

    def __getattr__ (self, attribute):
        return getattr (self._folder, attribute)
    
    @abstractmethod(callable)
    def establishConnection(db, server):
        pass