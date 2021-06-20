from django import template
import datetime
register = template.Library()

def replacestr(value):
    return value.replace('-', ' ')

def listify(value):
    return value.split()

def listin(value, index):
    return value[index]

def integer(value):
    return int(value)

def compare_datetime(value, time):
    main_time = time.replace(':', ' ').split()
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    task_year = int(value[0])
    task_month = int(value[1])
    task_day = int(value[2])
    task_hour = int(main_time[0])
    task_minute = int(main_time[1])
    task_time = datetime.datetime(task_year, task_month, task_day, task_hour, task_minute, 0)
    current_time = datetime.datetime(year, month, day, hour, minute, 0)
    if task_time > current_time:
        return True
    elif task_time < current_time:
        return False
    
register.filter('compare', compare_datetime)
register.filter('replacestr', replacestr)
register.filter('listify', listify)
register.filter('listin', listin)
register.filter('integer', integer)