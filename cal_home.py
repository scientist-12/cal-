from event import Event
from datetime import date, datetime

class Cal:
    def __init__(self):
        self.event_list = []
        # note about why this init is structured like this should be added

    def add_event(self, event):
        self.event_list.append(event)

    def get_events(self, date_str):
        date_str = datetime.strptime(date_str, '%Y-%m-%d').date()
        events = []
        for event in self.event_list:
            if event.date == date_str:
                events.append(event)
        return events
        # have this method explained in the file
        # also here's another sped up version:
        # return [event for event in self.event_list if event.date == date_str]