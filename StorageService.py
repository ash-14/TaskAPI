import json
import pickle

class StorageService:
    def __init__(self):
         self.__authenticationFile = "/data/AuthenticationFile.pickle"
         self.__usernameToFileNameMappingFile = "/data/UsernameToFileNameMappingFile.pickle"
        
    def updateAuthenticationFile(self, authenticationMappingJSON):
        fd = open(self.__authenticationFile, 'wb')
        pickle.dump(fd, authenticationMappingJSON)
        return
    
    def updateUsernameToFileNameMapppingFile(self, usernameToFileNameMappingJSON):
        fd = open(self.__usernameToFileNameMappingFile, 'wb')
        pickle.dump(fd, usernameToFileNameMappingJSON)
        return
    
    def loadUsernameToFileNameMappingFile(self):
        fd = open(self.__usernameToFileNameMappingFile, 'rb')
        jsonMap = pickle.load(fd)
        return jsonMap
    
    def loadAuthenticationFile(self):
        fd = open(self.__authenticationFile, 'rb')
        jsonMap = json.load(fd);
        return jsonMap
    
    def getUserSpace(self, username):
        filename, logFile = self.loadUsernameToFileNameMappingFile()[username]
        return filename, logFile
    
    def addUserSpace(self, username):
        usernameToFileNameMapping = self.loadUsernameToFileNameMappingFile()
        usernameToFileNameMapping[username] = ['/data/'+username+'_data.pickle', '/data/'+username+'.log']
        filename, logFile = usernameToFileNameMapping[username]
        self.updateUsernameToFileNameMapppingFile(usernameToFileNameMapping)
        self.storeTasks({}, filename)
        self.logEvent(logFile, "task created for user "+ username +"\n)
        return
    
    def logEvent(self, logFile, event):
        fd = open(logFile, 'a')
        fd.write(event + "\n")
        
    def storeTasks(self, listOfTasks, filename):
        fd = open(filename, 'wb')
        pickle.dump(fd, listOfTasks)
        
    def getTasks(self, filename):
        fd = open(filename, 'rb')
        return pickle.load(fd)
        
