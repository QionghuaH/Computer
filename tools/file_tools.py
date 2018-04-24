# -*- coding: utf-8 -*-
import os
import shutil
import time
from multiprocessing import Process
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_img_list(dir,img_list):
    if os.path.isfile(dir):
        img_list.append(dir) #encode('utf-8')) #decode('gbk').encode('utf-8'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            get_img_list(newDir,img_list)
    return img_list
        
def count_dirs(dir):
	#this is to count the number of files which is in the 'dir'
	subdirs=os.listdir(dir)
	subdirs.sort()
	count=len(subdirs)
	print dir,"has",count,"files"

def get_min_foder(dir,num):
	#dir is the fodler name
	#num is a threshold
	#return is if there exist a sundir of 'dir' contain images less than 'num'  
	#if file_num < num return num
	#else return -1
	subdirs=os.listdir(dir)
	subdirs.sort()
	for item in subdirs:
		subdir=os.path.join(dir,item)
		file_num=len(os.listdir(subdir))
		if(file_num<num): 
			return file_num
		else: continue
        return -1


	
def copy_folders_by_folderName(sub_folder,src_root,dst_root):
	src_folder = os.path.join(src_root, sub_folder)
	dst_folder = os.path.join(dst_root, sub_folder)
	if  os.path.exists(dst_folder):
		shutil.rmtree(dst_folder)
	shutil.copytree(src_folder,dst_folder)


def copy_folders_by_file(file_name,src_root,dst_root):
	t=time.time()
	'''
	'file_name' is a file that contain the subfolder of src_root and want to be moved
	file format
	  sub_folder1  1
	  sub_folder2  2
	  ... ...
	  sub_foldern  n
	  '''
	procs = []
	
	with open(file_name) as f:
		num=0
		for line in f.xreadlines():
			line=line.split('\n')[0].split(' ')[0]
			num+=1
			if num%1000==0:
				print num,' folders have been processed!'
			proc = Process(target=copy_folders_by_folderName, args=(line, src_root,dst_root,))
			procs.append(proc)
			proc.start()

	for proc in procs:
		proc.join()

	print "copy_folders_by_file ",time.time()-t


def move_folders_by_folderName(sub_folder,src_root,dst_root):
	src_folder = os.path.join(src_root, sub_folder)
	dst_folder = os.path.join(dst_root, sub_folder)
	if  os.path.exists(dst_folder):
		shutil.rmtree(dst_folder)
	shutil.move(src_folder,dst_folder)

def move_folders_by_file(file_name,src_root,dst_root):
	t=time.time()
	'''
	'file_name' is a file that contain the subfolder of src_root and want to be moved
	file format
	  sub_folder1  1
	  sub_folder2  2
	  ... ...
	  sub_foldern  n
	  '''
	procs = []
	
	with open(file_name) as f:
		num=0
		for line in f.xreadlines():
			line=line.split('\n')[0].split(' ')[0]
			if line=='':
				continue  # for the last line
			num+=1
			if num%1000==0:
				print num,' folders have been processed!'
			proc = Process(target=move_folders_by_folderName, args=(line, src_root,dst_root,))
			procs.append(proc)
			proc.start()

	for proc in procs:
		proc.join()

	print "move_folders_by_file ",time.time()-t
def copy_images_to_one_folder(src_folder,dst_folder):
    img_list=get_img_list(src_folder,[])
    print len(img_list) 
    for item in img_list:
        #if  os.path.exists(dst_folder):
        #        shutil.rmtree(dst_folder)
        shutil.copy(item,dst_folder)
    
if  __name__=='__main__':
	# file_name='VGGFace2_LFW_overlap.txt'
	# src_root='/DATACENTER2/qionghua.he/data/VGGFace/train_overlap_/'
	# dst_root='/DATACENTER2/qionghua.he/data/VGGFace/train_overlap/'
	# move_folders_by_file(file_name,src_root,dst_root)
        #get_min_foder(dir,num)
        copy_images_to_one_folder(r'/DATACENTER1/qionghua.he/data/HuiFu/汇富v2/Frames_ssd',r'/DATACENTER2/qionghua.he/data/HuiFu/汇富v2/test')
