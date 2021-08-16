import time

from datetime import datetime

# when you instantiate a TimeLog object, the timer starts ticking
class TimeLog:
    
    def __init__(self) -> None:
        self.startt = float()
        self.endt = float()
        self.log_file = r'R:\Administrative\Computer & Phone Systems\Ethan Scripts\time_log.txt'
        self.total = float()
        self.file_object = open(self.log_file, 'a') # open log file for appending



    def start(self):
        self.startt = time.time()
        print('start: ',self.startt)

    def end(self):
        self.endt = time.time()
        print('end: ',self.endt)
        self.total = self.endt - self.startt
        self.total = round(self.total, 2)

    def get_total(self):
        return self.total

    def write_log(self):
        today = datetime.today()
        message = today.strftime("%m/%d/%y %H:%M") + " execution time(s):  " + str(self.total) + "\n"
        self.file_object.write(message)



if __name__ == '__main__':



    t = TimeLog() # start timer

    t.start()

    start = time.time()

    for x in range(10000):
        for x in range(3000):
            pass

    end = time.time()

    total = end - start 
    total = round(total,2)
    print(total)

    t.end()


    print(t.get_total())

    t.write_log()