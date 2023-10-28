# Program to calculate what times I need to wake up and leave for an event
# Calculate wake-up time, get-up time, and leave time
# Enter arrival time, travel duration, plus shower and meal options
import datetime

# standard durations
shower = datetime.timedelta(minutes=30)
lunch = datetime.timedelta(minutes=35)
buffer = datetime.timedelta(minutes=10)
gettingReadyTime = datetime.timedelta(minutes=30)
wakingUpTime = datetime.timedelta(minutes=30)

# input: arrival time, travel duration
def time_input(t):
    y = datetime.datetime.strptime(t, '%I:%M %p')
    return y


def time_output(t):
    z = datetime.datetime.strftime(t, '%I:%M %p')
    return z


def duration_input(d):
    y = datetime.datetime.strptime(d, '%M')
    z = datetime.timedelta(minutes=y.minute)
    return z


eventStart = input(f'Event start time: ')
eventStart = time_input(eventStart)

travelDuration = input(f'How long it takes to get there: ')
travelDuration = duration_input(travelDuration)

timeToLeave = eventStart - travelDuration - buffer
timeToGetUp = timeToLeave - gettingReadyTime

showerQuestion = input(f'Shower? ')
if showerQuestion == 'y':
    timeToGetUp = timeToGetUp - shower

lunchQuestion = input(f'Lunch? ')
if lunchQuestion == 'y':
    timeToGetUp = timeToGetUp - lunch

alarmSet = timeToGetUp - wakingUpTime

print('Departure time: ' + time_output(timeToLeave) +
      '\nTime to get up: ' + time_output(timeToGetUp) +
      '\nSet your alarm for: ' + time_output(alarmSet))
