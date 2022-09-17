from datetime import datetime, timedelta
from objects import RemindWindow
import re

def start_notif() -> tuple[int, str] | None:
    time = input('Input time (hour:minutes:seconds): ')
    time = [el for el in time.split(':') if el!='']  # getting every split value if it is not ''
    time = time[:3 - (3 - len(time))] + ['0' for _ in range(3 - len(time))]  # set '0' to time unit that wasn't added
    for i, timeU in enumerate(time):
        try:
            u, m = {0:['Hours', 24], 1:['Minutes', 60], 2:['Seconds', 60]}[i]  # dict with unit name, and max time
            if not (0 <= int(timeU) <= m):
                print(f'{u} must be from 0 to {m}')
                return
            time[i] = int(time[i])
        except ValueError:  # if some time unit isn't number it will give ValueError in "if not (0 <= int(timeU) <= m)"
            print('You must write only numbers.')
            return

    reminder = input('Input reminder: ')
    if not len(reminder) <= 150:
        print("Too long text, it must not be longer than 150 characters")
        return

    return (time[0]*60*60)+(time[1]*60)+(time[2]), reminder  # return time in second and reminder


def now_time() -> int:
    time = datetime.now()

    return (time.hour*60*60)+(time.minute*60)+(time.second)  # return time in second


def get_time_from_seconds(secs: int) -> tuple[int]:
    time = str(timedelta(seconds=secs))
    reg = re.search(r"((?P<days>\d*) days?, )?(?P<hour>\d+):(?P<mins>\d+):(?P<secs>\d+)", time)
    d,h,m,s = reg.group('days'), reg.group('hour'), reg.group('mins'), reg.group('secs')
    if d is None: d = 0
    return d,h,m,s

def get_time_to_reminder(notify_time: int, moment_time: int) -> int:
    time = notify_time-moment_time
    if time < 0: time=24*60*60-moment_time+notify_time
    return time

def remind(remind_text):
    win = RemindWindow(remind_text)
    win.run()