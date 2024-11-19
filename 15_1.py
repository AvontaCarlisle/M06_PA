import multiprocessing
import time
import random
from datetime import datetime


def worker():
    wait_time = random.randint(1,3)
    time.sleep(wait_time)
    print(f"Proccess ID : {multiprocessing.current_process().pid} Time: {datetime.now}")


if __name__ == '__main__':
    proccesses = []


    for _ in range(3):
        process = multiprocessing.Process(target=worker)
        proccesses.append(process)
        process.start()

    for process in proccesses:
        process.join()