#!/usr/bin/python  
# -*- coding: utf-8 -*-
#2017.12.26 by qionghua.he
import sys
import os
import re
import chardet
import codecs 

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #ignore these File
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList


# in_file format is 'id name'
# return name_map the form is name_map[id]=name
def get_name_map(in_file):
    name_map={}
    f=open(in_file,'r')
    for line in f.xreadlines():
        line=line.strip('\n').split(' ') 
        name_map[line[0]]=line[1]
    return name_map

def WriteFileList(dir, fileList,label,data_set):
    category=dir.split("/")[-1]
   
    n=len(fileList)
    #n=100
    m=int(n*0.95)#0.7
    l=int(n*1)#n*0.8
    
    pair=open("pair_"+data_set+".txt","a")
    pair.write(category+" "+ label+"\n")
    pair.close()
    
    file = open("train_"+data_set+".txt","a") 
    for i in range(m):
        file.write(dir+"/"+os.path.basename(fileList[i]) +' '+label+'\n')
    file.close()

    val=open("val_"+data_set+".txt","a") 
    for i in range(m,l):
        val.write(dir+"/"+os.path.basename(fileList[i]) +' '+label+'\n')
    val.close()

    #write test file
    file = open("test_"+data_set+".txt","a") 
    for i in range(l,n):
       file.write(dir+"/"+os.path.basename(fileList[i]) +' '+label+'\n')
    file.close()
    
if __name__=='__main__':
    #RootDir="/DATACENTER2/qionghua.he/data/MS_CELEB/MTCNN-Faces-Aligned1.1_10K"
    RootDir="/DATACENTER2/qionghua.he/data/MS_CELEB/unclean1.2_10K_0.4_clean/"
    data_set=10000

    name_map1=get_name_map('/home/qionghua.he/data/tools/LFW_MS_overlap.txt')
    name_map2=get_name_map('/home/qionghua.he/data/tools/facescrub_MS_overlap.txt')
    name_map3=get_name_map('/home/qionghua.he/data/tools/YTF_MS_overlap.txt') 
    if os.path.isdir(RootDir):
        label=0
        categories=os.listdir(RootDir)
        categories.sort()
        for s in categories:
            #find the one belongs to LFW & faceScrub
            tmp=name_map1.get(s, None)
            if (tmp!=None): 
                #print s
                continue
            tmp=name_map2.get(s, None)
            if (tmp!=None): continue
            
            tmp=name_map3.get(s, None)
            if (tmp!=None): continue            

            Dir=os.path.join(RootDir,s)
            if not os.path.isfile(Dir):
                list = GetFileList(Dir, [])
                #if len(list)<75: continue #list length<20,then the folder wont used for training
                #else:
                WriteFileList(Dir,list,str(label),str(data_set))
                label=label+1
                if(label==data_set): break
        print label
    print 'Write Output.txt Done!!!'
