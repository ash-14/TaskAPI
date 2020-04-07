import json
import pickle

class StorageService:
    def __init__(self):
         self.__authenticationFile = "AuthenticationFile.py"
         self.__usernameToFileNameMappingFile = "UsernameToFileNameMappingFile.py"
        
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
    
    def logEvent(self, logFile, event):
        fd = open(logFile, 'w')
        fd.write(event + "\n")
        
    def storeTasks(self, listOfTasks, filename):
        fd = open(filename, 'w')
        pickle.dumps(fd, listOfTasks)
        
    def getListOfTasks(self, username):
        
