from functions import *
from time import sleep

def main():
    try: remind_time, remind_text = start_notif()
    except TypeError: return  # if except TypeError than user input incorrect info and function return None (python couldn't unpack None and raise error)

    time_to_remind = get_time_to_reminder(remind_time, now_time())
    d,h,m,s = get_time_from_seconds(time_to_remind)
    print(f"You'll be notified after {d} days, {h} hours, {m} minutes, {s} seconds.")
    sleep(time_to_remind)
    remind(remind_text)

if __name__ == '__main__':
    main()