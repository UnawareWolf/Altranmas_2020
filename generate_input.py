import os
import sys
import getopt
import random
import hashlib

CHAR_LIST = ["^", "v", ">", "<"]
START = 7000
STOP = 9000

def get_input_name(path):
    filename, extension = os.path.splitext(path)
    count = 1

    while os.path.exists(path):
        path = f"{filename}_{count}{extension}"
        count += 1
    
    return path

def generate_data():
    return "".join([
        random.choice(CHAR_LIST)
        for _ in range(random.randint(START, STOP))])

def create_file(path):
    with open(path, "w") as f:
        f.write(generate_data())

def set_seed(name):
    random.seed(int(hashlib.sha256(name.encode('utf-8')).hexdigest(), 16))

def run(name=None):
    if name is not None:
        set_seed(name)
        path = get_input_name(f"./{name}_input.txt")
    else:
        path = get_input_name("./input.txt")

    create_file(path)

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["name="])
    except getopt.GetOptError:
        print('generate_input.py --name <inputfile>')
        sys.exit(2)
    
    name = None
    for opt, arg in opts:
        if opt == "--name":
            name = arg

    run(name)
