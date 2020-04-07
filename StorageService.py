import json
import pickle

class StorageService:
    def __init__(self):
         self.__authenticationFile = "AuthenticationFile.py"
         self.__usernameToFileNameMappingFile = "UsernameToFileNameMappingFile.py"
        
    def updateAuthenticationFile(self, authenticationMappingJSON):
        fd = open(self.__authenticationFile, 'w')
        pickle.dump(fd, authenticationMappingJSON)
        return
    
    def updateUsernameToFileNameMapppingFile(self, usernameToFileNameMappingJSON):
        fd = open(self.__usernameToFileNameMappingFile, 'w')
        pickle.dump(fd, usernameToFileNameMappingJSON)
        return
    
    def loadUsernameToFileNameMappingFile(self):
        fd = open(self.__usernameToFileNameMappingFile, 'r')
        jsonMap = pickle.load(fd)
        return jsonMap
    
    def loadAuthenticationFile(self):
        fd = open(self.__authenticationFile, 'r')
        jsonMap = json.load(fd);
        return jsonMap
    
    def getUserSpace(self, username):
        filename, logFile = self.loadUsernameToFileNameMappingFile()[username]
        return filename, logFile
    
    def logEvent(self, logFile, event):
        fd = open(logFile, 'w')
        fd.write(event + "\n")
        
    def storeTasks(self, listOfTasks, filename):
        fd = open(filename, 'w')
        pickle.dump(fd, listOfTasks)
        
    def getListOfTasks(self, filename):
        fd = open(filename, 'r')
        return pickle.load(fd)
        
