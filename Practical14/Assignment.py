#!/usr/bin/env python
from xml.dom import minidom
#import os
from typing import List
import pandas
#os.chdir('D:\\Smst2\\IBI1B\\IBI1_2019-20\\Practical14')
DT=minidom.parse('go_obo.xml')
root = DT.documentElement
terms = root.getElementsByTagName("term")
class afinfo:
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.id
    def __init__(self,id:str,name:str,defstr:str,is_a:List[str]):
        self.id=id
        self.name=name
        self.defstr=defstr
        self.is_a=is_a
        self.dep=0
    def build_dep(self,my_list:List[__init__])->int:
        if self.dep == 0:
            for item in my_list:
                if item.is_a.__contains__(self.id):
                    item.build_dep(my_list)
                    self.dep=self.dep+item.dep+1
        return self.dep
af:List[afinfo]=[]
af_all:List[afinfo]=[]
for item in terms:
    tmpds=[]
    for is_a in item.getElementsByTagName('is_a'):
        tmpds.append(is_a.childNodes[0].data)
    tmp_af=afinfo(item.getElementsByTagName('id')[0].childNodes[0].data,item.getElementsByTagName('name')[0].childNodes[0].data,item.getElementsByTagName('def')[0].getElementsByTagName('defstr')[0].childNodes[0].data,tmpds)
    if tmp_af.defstr.__contains__('autophagosome'):
        af.append(tmp_af)
    af_all.append(tmp_af)
del DT, root, terms,tmpds,is_a
ID=[]
NAME=[]
DEF=[]
CN=[]
for item in af:
    ID.append(item.id)
    NAME.append(item.name)
    DEF.append(item.defstr)
    item.build_dep(af_all)
    CN.append(item.dep)
D={'id':ID,'name':NAME,'definition':DEF,'child_nodes':CN}
DF=pandas.DataFrame.from_dict(D)
DF.to_excel('autophagosome.xlsx')
