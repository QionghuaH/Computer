#-*-coding:utf-8-*-
import sys
import os
import cv2
import shutil
from multiprocessing import Process
import threading
import time

'''
THRESHOLD = 40.0

dst_root = r'F:/HQH/code/tools/DataClean/images_'
src_root='F:/HQH/code/tools/DataClean/images/'
t=time.time()
for fpath, dirs, fs in os.walk(src_root):
    i = 0
    for dir in dirs:
        i += 1
        if i%100 == 0:
            print (str(i)+'folders processed current:'+dir)
        abs_dir = os.path.join(fpath, dir)
        for _, __, fs in os.walk(abs_dir):
            clear_img_list = []
            for f in fs:
                item = os.path.join(_, f)
                image = cv2.imread(os.path.join(src_root, item))
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                imageVar = cv2.Laplacian(gray, cv2.CV_64F).var()
                if not imageVar < THRESHOLD:
                    clear_img_list.append(item)
            print len(fs),len(clear_img_list)
            dst_folder = os.path.join(dst_root, dir)
            if len(clear_img_list) >= 15:
                if not os.path.exists(dst_folder):
                    os.makedirs(dst_folder)
                for item in clear_img_list:
                    dst_path = os.path.join(dst_folder, item.split('\\')[-1])
                    shutil.copy(item, dst_path)
print time.time()-t

'''			
def remove_blur(dir, src_root, dst_root, THRESHOLD ):
    abs_dir = os.path.join(src_root, dir)
    for _, __, fs in os.walk(abs_dir):
        clear_img_list = []
        for f in fs:
            item = os.path.join(_, f)
            image = cv2.imread(os.path.join(src_root, item))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            imageVar = cv2.Laplacian(gray, cv2.CV_64F).var()
            if not imageVar < THRESHOLD:
                clear_img_list.append(item)
        #print len(fs),len(clear_img_list)
        dst_folder = os.path.join(dst_root, dir)
        if len(clear_img_list) >= 30:
            if not os.path.exists(dst_folder):
                os.makedirs(dst_folder)
            for item in clear_img_list:
                dst_path = os.path.join(dst_folder, item.split('/')[-1]) #'/' different from win
                shutil.copy(item, dst_path)



#according the given txt				
if __name__ == "__main__":
    procs = []
    THRESHOLD = 40.0
    src_root = r'/DATACENTER2/qionghua.he/data/MS_CELEB/MTCNN-Faces-Aligned1.0/'
    dst_root = r'/DATACENTER2/qionghua.he/data/MS_CELEB/MTCNN-Faces-Aligned1.1/'
	
    t=time.time()
    f=open('/home/qionghua.he/projects/caffe-face/face_example/data/pair_30000.txt')
    i = 0
    for line in f.xreadlines():
        dir=line.split(' ')[0]
        i+=1
        if i%100 == 0:
            print (str(i)+'folders processed current:'+dir)
        proc = Process(target=remove_blur, args=(dir, src_root, dst_root,THRESHOLD ,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
    print "Remove_Bluer Done. ",time.time()-t

'''	
#according the given path
if __name__ == "__main__":
    procs = []
    THRESHOLD = 40.0

    dst_root = r'F:/HQH/code/tools/DataClean/images_'
    src_root='F:/HQH/code/tools/DataClean/images/'
	
    t=time.time()
    for fpath, dirs, fs in os.walk(src_root):
        i = 0
        for dir in dirs:
            #print dir
            i+=1
            if i%100 == 0:
                print (str(i)+'folders processed current:'+dir)
            proc = Process(target=remove_blur, args=(dir, src_root,dst_root,THRESHOLD ,))
            procs.append(proc)
            proc.start()
    for proc in procs:
        proc.join()
    print "Remove_Bluer Done. ",time.time()-t
'''
