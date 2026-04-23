from event import Event
from datetime import date, datetime
import json

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

    def save_to_js(self, filename):
        js_events = []  # Good to note that creating the list outside the loop, means it outlives the loop
                        # no need to return anything from the loop just continue with the method
        for event in self.event_list:
            conv = event.to_dict()
            js_events.append(conv)
                        # an easier way to write this would be js_events.append(event.to_dict())
        with open(filename, 'w') as f:
            json.dump(js_events, f, indent=4)
        '''
        the fn json.dump, takes two arguments, the data you want to write
        and the file you want to write to, and combines them to in one 
        single fn. You must import json for this as demonstrated at the top 
        of the file.
        '''

    def js_to_py(self, filename):
        conv_events = []
        with open(filename, 'r') as f:
            data = json.load(f)
            for event in data:
               js_dat = Event(event['name'], event['date'],
                              event['time'], event['desc'],
                              event['noti_delay'])
               conv_events.append(js_dat)
            self.event_list = conv_events
        return self.event_list
            # remember to add a docstring for each method explaining its function