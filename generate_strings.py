import random
import string

characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'
sizes = {'1kb': 1000, "10kb":10000, "100kb":100000, "1mb":1000000, "10mb":10000000, "100mb":100000000}

def generate_string(size):
    return ''.join(random.choices(characters, k=size))

def create_txt_files():
    for i in range(5):
        for key, value in sizes.items():
            with open("data/txt/" + key + '-' + str(i) +".txt", 'w') as f:
                f.write(generate_string(value))

create_txt_files()