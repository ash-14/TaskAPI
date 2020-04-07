class Task:
    def __init__(self, taskId, taskTitle, taskDueDate, taskStatus = 'Todo'):
        self.taskId = taskId
        self.taskTitle = taskTitle
        self.taskDueDate = taskDueDate
        self.taskStatus = taskStatus

    def getTaskId(self):
        return self.taskId
    
    def getTaskTitle(self):
        return self.taskTitle
    
    def getTaskDueDate(self):
        return self.taskDueDate
    
    def getTaskStatus(self):
        return self.taskStatus
    
    def setTaskId(self, taskId):
        self.taskId = taskId
    
    def setTaskDueDate(self, taskDueDate):
        self.taskDueDate = taskDueDate
    
    def setTaskTitle(self, taskTitle):
        self.taskStatus = taskStatus
        
    def setTaskStatus(self, taskStatus):
        self.taskStatus = taskStatus
    
