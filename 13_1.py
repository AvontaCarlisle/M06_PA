from datetime import datetime


def export_time():
    now = datetime.now()
    now_time = now.strftime("%Y/%m/%d %H:%M:S")
    with open("today.txt", 'w') as file:
        file.write(f'{now_time}')

export_time()