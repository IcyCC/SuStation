# -*- coding:utf-8 -*-
#该类用于处理数据
import json

def getID():
    with open('id.in') as f:
        a = f.read()
        return int(a)

def setID(a):
    with open('id.in', 'w') as f:
        f.write(str(a))

def getItem():
    with open('items.json') as InFile:
        return json.loads(InFile.read())



def outItem(id,url,score):
    with open('Output.json', 'a') as OutFile:
        dic = {"id":id,"url":url, "score":score}
        OutFile.write(json.dumps(dic)+',\n')

