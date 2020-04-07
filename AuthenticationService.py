import hashlib

class AuthenticationService:
    def __init__(self):
        self.__storageSystemClient = new StorageSystem();
        
    def authenticateUser(self, username, password):
        authenticationMap = self.__storageSystemClient.loadAuthenticationFile();
        if username in authenticationMap and authenticationMap[username] == password:
            return True
        return False
    
    def addUserCredentials(self, username, password):
        authenticationMap = self.__storageSystemClient.loadAuthenticationFile();
        if username not in authenticationMap:
            authenticationMap[username] = password
            self.__storageSystemClient.updateAuthenticationFile(authenticationMap)
            return True
        
        return False
