
from datetime import date, datetime

class Event:
    def __init__(self, name, date_str, time, desc, noti_delay):
        self.name = name
        self.date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # Get further explanation on this above later
        self.time = time
        self.desc = desc
        self.noti_delay = noti_delay

    def __str__(self):
        return f'{self.name} on {self.date} at {self.time}'

    def __repr__(self):
        return f'{self.name} on {self.date} at {self.time}'
        """
        When an object, like our event, live inside a container, like a list
        They need to be displayed in a different way, __str__ will not cut it
        that is what this __repr__ does for us 
        """
    def up_coming(self):
        if date.today() < self.date:
            return True
        else:
            return False
        # change to return date.today() < self.date / explain y