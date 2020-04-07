class TaskApp:
    def __init__(self, username):
        self.username = username
        self.storageServiceClient = new StorageService()
        self.filename, self.logFile = self.storageServiceClient.getUserSpace(username)
        return

    def add(self, title, dueDate):
        tasks = getTasks()
        task = new Task(len(tasks), title, dueDate)
        tasks[task.getTaskId()] = task
        storeTasks(tasks, self.filename)
        storageServiceClient.logEvent("Function --> add\n Task -->" + task +"\n")
        return

    # tasks is a dict of taskId and task Object
    def getTasks(self):
        tasks = self.storageServiceClient.getTasks(self, self.filename)
        return tasks

    def getTasks(self, dueDate):
        tasks = getTasks()
        tasksWithDueDate = []
        for taskId, task in enumerate(tasks):
            if(task.getTaskDueDate() == dueDate):
                tasksWithDueDate.append(task)
        return tasksWithDueDate

    def markTaskStatus(self, taskId, taskStatus):
        tasks = getTasks()
        tasks[taskId].setTaskStatus(taskStatus)
        storeTasks(tasks, self.filename)
        storageServiceClient.logEvent("Function --> add\n Task -->" + task +"\n")
        
