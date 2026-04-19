from cal_home import Cal
from event import Event

miles_cal = Cal()
'''
  So think of Cal() as a container of data, not necessarily a Calender.
  Yes, it function as your calender, but, technically on a ground-level,
  its just an empty list that's waiting to get events added to it. That's 
  why we have to call Cal() here and assign it to a variable, because we
  need an empty "calender" to put dates and events in to manipulate.
'''

b_day = Event('bday', '2027-03-24',
              '11:00 PM', 'MY BDAY FUCK YEAH',
              30)
reg = Event('Reg Opens', '2027-06-18',
            '9:00 AM', 'Registration Opens',
            30)

miles_cal.add_event(b_day)
miles_cal.add_event(reg)

print(miles_cal.get_events('2027-03-24'))
print(miles_cal.get_events('2027-06-18'))






