from datetime import datetime


def import_time():
    with open('today.txt', 'r') as file:
        today_string = file.read()
        return today_string
    

def parse_time(today_string):
    time_format = "%Y-%m-%d %M:%H:%S"
    parse = datetime.strftime(today_string, time_format)
    print(f"The current time and date is {parse}")


parse_time(import_time())