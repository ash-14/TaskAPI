import json
import pickle

class StorageService:
    def __init__(self):
         self.__authenticationFile = "/data/AuthenticationFile.py"
         self.__usernameToFileNameMappingFile = "/data/UsernameToFileNameMappingFile.py"
        
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
    
    def addUserSpace(self, username):
        usernameToFileNameMapping = self.loadUsernameToFileNameMappingFile()
        usernameToFileNameMapping[username] = ['/data/'+username+'_data', '/data/'+username+'_log']
        filename, logFile = usernameToFileNameMapping[username]
        self.updateUsernameToFileNameMapppingFile(usernameToFileNameMapping)
        self.storeTasks({}, filename)
        self.logEvent(logFile, "task created for user "+ username +"\n)
        return
    
    def logEvent(self, logFile, event):
        fd = open(logFile, 'a')
        fd.write(event + "\n")
        
    def storeTasks(self, listOfTasks, filename):
        fd = open(filename, 'w')
        pickle.dump(fd, listOfTasks)
        
    def getTasks(self, filename):
        fd = open(filename, 'r')
        return pickle.load(fd)
        
