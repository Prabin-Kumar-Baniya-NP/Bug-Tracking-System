import random
import datetime

def ticket_number_generator():
    random_number = str(random.randrange(1,9999,21))
    date_time = datetime.datetime.now()
    ticket_number = date_time.strftime("%Y%m%d%H%M%S") + random_number
    return ticket_number