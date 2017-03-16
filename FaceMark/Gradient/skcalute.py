from __future__ import division
import json
import pandas as pa
import numpy as np
from DateProcess import InDate
import matplotlib.pyplot as plt
from sklearn import linear_model as lm
from sklearn.decomposition import PCA

#InDate.process(Inpath="../Date/Output.json",Xpaht="../Date/X.json",Ypath="../Date/Y.json")
#pca1=PCA(n_components=100)
#pca2=PCA(n_components=100)
#newData=pca1.fit_transform(InDate.load_date("../Date/X.json"))
InDate.saveWithUrl(img_url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1489682143944&di=f6eac684e1bb8b318aa5bfb183a0e514&imgtype=0&src=http%3A%2F%2Fwww.hinews.cn%2Fpic%2F0%2F15%2F05%2F54%2F15055407_939404.jpg",path="../Date/test.json")
X=InDate.load_date("../Date/X.json")
y= InDate.load_date("../Date/Y.json")
test=InDate.load_date("../Date/test.json")
#newDataT = pca2.fit_transform(InDate.load_date("../Date/test.json"))
re = lm.LinearRegression(normalize=True)

re.fit(X,y)
print re.predict(test)
