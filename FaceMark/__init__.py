import json
import numpy as np
from DateProcess import InDate
from Gradient import Gradient

def train(alpha,num_iters,train_set,x_file,y_file,theta_file):
    ## train function
    ## parameters is  path

    InDate.process(Inpath = train_set,Xpaht = x_file,Ypath = y_file)
    save(theta_file,Gradient.GradientDescent(X=InDate.load_date(x_file),y=InDate.load_date(y_file),alpha=alpha,num_iters=num_iters))

def mark(image_url,theta_file):
    theta = InDate.load_date(theta_file)
    X= InDate.get_Xlist(image_url)
    X = np.array(InDate.load_date('Date/test.json'))
    X.shape = (1,X.shape[0])
    l = Gradient.Normalization(InDate.load_date('Date/X.json'),InDate.load_date('Date/Y.json'))
    X = (X-l[2][0])/l[2][1]
    score = np.dot(X,theta)*l[3][1]+l[3][0]
    return score


def save(path,theta):
    with open(path,'w') as f:
        f.write(json.dumps(theta.tolist()))


print mark('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1489549067407&di=b8822dfa6849b5e32ae38ea01811519f&imgtype=0&src=http%3A%2F%2Fpic18.photophoto.cn%2F20110120%2F0036036748117379_b.jpg','Date/theta.json')