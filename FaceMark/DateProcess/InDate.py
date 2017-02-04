import json
import numpy as np
import requests
import matplotlib.pyplot as plt

OriginXFile = None

def dist(x1,y1,x2,y2,):
    # type: (object, object, object, object) -> object
    return ((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2) ** 0.5

def get_orgin(image_url):
    ## get orgin json file from api
    url = 'https://api.aofei.org/facepp/detect'
    date = {'image_url': image_url,'return_landmark': True,'return_attributes':'gender'}
    r = requests.post(url=url, data=date,verify=False)
    return r.json()

def get_landmark(image_url):
    ## from orgin json file get land mark
    # for item in get_landmark('http://oss.aofei.org/images/lyf.jpg').items():
    #     x = item[1]['x']
    #     y = item[1]['y']
    #     label = str(item[0])
    return get_orgin(image_url=image_url)['faces'][0]


def plot_landmark(image_url = None):
    ## draw a picture which have a face and landmark
    plt.figure()
    plt.imshow(plt.imread('a.jpg'))
    for item in get_landmark('https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2737886401,2067163053&fm=23&gp=0.jpg')['landmark'].items():
        x = item[1]['x']
        y = item[1]['y']
        label = str(item[0])
        plt.scatter(x, y)
        plt.text(x, y,str(label),fontsize = 8,verticalalignment='center',color='red',fontweight= 'demi')

    plt.show()

def get_Xlist(image_url):
    dic = get_landmark(image_url)
    regular = {'width':dic['face_rectangle']['width'], 'height':dic['face_rectangle']['height']}
    dic = dic['landmark']
    Xlist = [1]
    ###pick eye key distance
    lefteye_width = dist(x1=dic['left_eye_left_corner']['x'],y1=dic['left_eye_left_corner']['y'],\
                         x2=dic['left_eye_right_corner']['x'],y2=dic['left_eye_right_corner']['y'])/regular['width']
    Xlist += [lefteye_width]
    righteye_width = dist(x1=dic['right_eye_left_corner']['x'], y1=dic['right_eye_left_corner']['y'], \
                         x2=dic['right_eye_right_corner']['x'], y2=dic['right_eye_right_corner']['y'])/regular['width']
    Xlist += [righteye_width]
    lefteye_height = dist(x1=dic['left_eye_top']['x'], y1=dic['left_eye_top']['y'], \
                         x2=dic['left_eye_bottom']['x'], y2=dic['left_eye_bottom']['y'])/regular['height']
    Xlist += [lefteye_height]
    righteye_height = dist(x1=dic['right_eye_top']['x'], y1=dic['right_eye_top']['y'], \
                         x2=dic['right_eye_bottom']['x'], y2=dic['right_eye_bottom']['y'])/regular['height']
    Xlist += [righteye_height]
    ### pick head key distance
    for i in range(1,10):
        Xlist += [dist(x1=dic['contour_left%d'%i]['x'], y1=dic['contour_left%d'%i]['y'], \
                    x2=dic['contour_right%d'%i]['x'], y2=dic['contour_right%d'%i]['y'])/regular['width']]
    ### pick nose key distance
    nose_width1 = dist(x1=dic['nose_left']['x'], y1=dic['nose_left']['y'], \
                         x2=dic['nose_right']['x'], y2=dic['nose_right']['y'])/regular['width']
    Xlist += [nose_width1]
    nose_width2 = dist(x1=dic['nose_contour_left2']['x'], y1=dic['nose_contour_left2']['y'], \
                         x2=dic['nose_contour_right2']['x'], y2=dic['nose_contour_right2']['y'])/regular['width']
    Xlist += [nose_width2]
    nose_height = dist(x1=dic['nose_tip']['x'], y1=dic['nose_tip']['y'], \
                         x2=dic['nose_contour_lower_middle']['x'], y2=dic['nose_contour_lower_middle']['y'])/regular['height']
    Xlist += [nose_height]
    ### pick mouth key distance
    mouth_width = dist(x1=dic['mouth_left_corner']['x'], y1=dic['mouth_left_corner']['y'], \
                         x2=dic['mouth_right_corner']['x'], y2=dic['mouth_right_corner']['y'])/regular['width']
    Xlist += [mouth_width]
    mouth_height1= dist(x1=dic['mouth_upper_lip_top']['x'], y1=dic['mouth_upper_lip_top']['y'], \
                         x2=dic['mouth_upper_lip_bottom']['x'], y2=dic['mouth_upper_lip_bottom']['y'])/regular['height']
    Xlist += [mouth_height1]
    mouth_height2= dist(x1=dic['mouth_lower_lip_top']['x'], y1=dic['mouth_lower_lip_top']['y'], \
                         x2=dic['mouth_lower_lip_bottom']['x'], y2=dic['mouth_lower_lip_bottom']['y'])/regular['height']
    Xlist += [mouth_height2]
    #Xlist = map_features(Xlist)
    return Xlist

def map_features(list):
    ## combine features
    length = len(list)
    for x in range(length):
        for y in range(x,length):
            list += [list[x]/list[y]]
    return list

def process(Inpath,Xpaht = 'X.json',Ypath = 'Y.json'):
   ## process Date output can be used to train
    Y = []
    X = []
    with open(Inpath,'r') as infile:
        indate = json.loads(infile.read())
    for dic in indate:
        Y += [[dic['score']]]
        X += [get_Xlist(dic['url'])]
    with open(Ypath,'w') as yfile:
        yfile.write(json.dumps(Y))
    with open(Xpaht,'w') as xfile:
        xfile.write(json.dumps(X))

def load_date(path):
    # this function is aim to trans X.json to numpy m*d matrix
    with open(path, 'r') as f:
        Xdate = json.loads(f.read())
        X = np.array(Xdate, dtype=np.float)
        return X
