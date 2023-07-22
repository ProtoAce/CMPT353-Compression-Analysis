import random
import string

characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

def generate_string(size):
    return ''.join(random.choices(characters, k=size))

def create_txt_file(size, file_name):
    with open(file_name, 'w') as f:
        f.write(generate_string(size))

create_txt_file(1000000000, './data/txt/1gb_generated.txt')