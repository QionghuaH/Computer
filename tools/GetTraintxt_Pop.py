#!/usr/bin/python  
# -*- coding: utf-8 -*-
#2017.11.24 by qionghua.he
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

def get_MS_name():
    name_map={}
    f=open("./Top1M_MidList.Name.tsv",'r')
    #f=open("./Top100.tsv",'r')
    for line in f.xreadlines():
        line=line.strip('\n').split('\t')
        pattern=re.compile('\".*\"@')
        #code_type=chardet.detect(line[1])['encoding']#.encode('utf-8')
        #print code_type
        tmp=re.findall(pattern,line[1])
        tmp=tmp[0][1:-2]
        name_map[tmp]=line[0]
    f.close()
    return name_map

def find_same(name_map,file_name='./star_name.txt'):
    f=open(file_name,'r')
    fout=open('./Pop_Star.txt','w')
    for line in f.xreadlines():
        line=line.strip('\n')
        code_type=chardet.detect(line)
        #print code_type
        tmp=name_map.get(line, None)
        if(tmp!=None):
            fout.write(tmp+' "'+line+'"\n')
    f.close()
    fout.close()
    
    
def get_train_txt_pop(input_file,output_file,dateset,root_path):
    #get the category from the input file
    #save all the path of image in the choose category to output_file
    #dateset is the number of category
    #root_path is the root path of the train dataset

    i=0
    j=0
    fin=open(input_file,'r')
    fout=open(output_file,'w')
    for line in fin.xreadlines():
        if i==dateset:
            break
        line=line.strip('\n').split(' ')[0]
        path=root_path+line+'/'
        fileList=[]
        fileList=GetFileList(path, fileList)
        if len(fileList)==0:
            j+=1
        else:
            i+=1
        for item in fileList:
            fout.write(item+' '+str(i)+'\n')
        
    print dateset-i, 'categories missed in ',dateset,'categories'
    fin.close()
    fout.close()
        
        
    
    
if __name__=='__main__':
    
    #name_map=get_MS_name()
    #find_same(name_map,"./star_name.txt")

    # 
    input_file='Pop_Star.txt'
    output_file='train_txt_Pop.txt'
    dateset=10000
    root_path='/DATACENTER2/qionghua.he/data/MS_CELEB/MTCNN-Faces-Aligned1.0/'
    get_train_txt_pop(input_file,output_file,dateset,root_path)
    
    print '--------Done!----------------'
