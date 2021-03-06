import hashlib

class AuthenticationService:
    def __init__(self):
        self.storageSystemClient = StorageSystem();
        
    def authenticateUser(self, username, password):
        authenticationMap = self.storageSystemClient.loadAuthenticationFile();
        if username in authenticationMap and authenticationMap[username] == password:
            return True
        return False
    
    def addUserCredentials(self, username, password):
        authenticationMap = self.storageSystemClient.loadAuthenticationFile();
        if username not in authenticationMap:
            authenticationMap[username] = password
            self.storageSystemClient.updateAuthenticationFile(authenticationMap)
            self.storageSystemClient.addUserSpace(username)
            return True
        return False
