import json
import numpy as np

OriginXFile = None

def get_date():
    pass

def process_date():
    pass


def load_date(path):
    # this function is aim to trans X.json to numpy m*d matrix
    with open(path,'r') as f:
        Xdate = json.loads(f.read())
        X = np.array(Xdate,dtype=np.float)
        return X

