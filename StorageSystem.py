import json
import pickle

class StorageSystem:
    def __init__(self):
         self.__authenticationFile = "authenticationFile.py"
         self.__usernameToFileNameMappingFile = "usernameToFileNameMappingFile.py"
        
    def updateAuthenticationFile(self, authenticationMappingJSON):
        fd = open(self.__authenticationFile, 'w')
        json.dumps(fd, authenticationMappingJSON)
        return
    
    def updateUsernameToFileNameMapppingFile(self, usernameToFileNameMappingJSON):
        fd = open(self.__usernameToFileNameMappingFile, 'w')
        json.dumps(fd, usernameToFileNameMappingJSON)
        return
    
    def loadUsernameToFileNameMappingFile(self):
        fd = open(self.__usernameToFileNameMappingFile, 'r')
        jsonMap = json.loads(fd);
        return jsonMap
    
    def loadAuthenticationFile(self):
        fd = open(self.__authenticationFile, 'r')
        jsonMap = json.loads(fd);
        return jsonMap
    
    def getUserSpace(self, username):
        filename, logFile = self.loadUsernameToFileNameMappingFile()
        return filename, logFile
    
    def logEvent(logFile, event):
        fd = open(logFile, 'w')
        fd.write(event + "\n")
        
