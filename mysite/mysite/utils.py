import random
import string

from demoapp.models import Notification

def get_str(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
for i in range(10000):
    Notification.objects.create(text=get_str(300),link="https://acc"+get_str(100),ntype=get_str(100),description=get_str(1400))