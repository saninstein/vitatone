import random
import string

def get_uniq_name(instance, filename):
    new_name = ''.join(random.sample(string.ascii_lowercase, 15))
    new_name += filename[filename.find('.'):]
    return new_name