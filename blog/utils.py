import random
import string

def get_uniq_name(instance, filename):
    new_name = ''.join(random.sample(string.ascii_lowercase, 15))
    new_name += filename[filename.find('.'):]
    return new_name

def get_image_path(inst, name):
    return f"{type(inst).__name__}_{inst.pk}/{get_uniq_name(inst, name)}"