class Logger:
    def __init__(self, filename='../data/log.txt'):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as file:
            file.write(message + '\n')