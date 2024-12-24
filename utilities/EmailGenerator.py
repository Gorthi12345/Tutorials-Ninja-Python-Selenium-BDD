from datetime import datetime


def Getting_email():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "redsea" + time_stamp + "@gmail.com"