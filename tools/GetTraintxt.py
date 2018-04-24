import os
#from PIL import Image
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk').encode('utf-8'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #ignore these File
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList
	
	
def WriteFileList(dir, fileList,label,data_set):
    category=dir.split("/")[-1]
   
    n=len(fileList)
    m=int(n*0.9)#0.7
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
    
RootDir="/DATACENTER2/qionghua.he/data/MS_CELEB/MTCNN-Faces-Aligned1.0/"
# RootDir="/home/heqionghua/data/MS_CELEB/MXNet-MTCNN-Faces-Aligned-Clean/"
data_set=10000
if os.path.isdir(RootDir):
    label=0
    categories=os.listdir(RootDir)
    categories.sort()
    for s in categories:
        Dir=os.path.join(RootDir,s)
        if not os.path.isfile(Dir):
            list = GetFileList(Dir, [])
            if len(list)<50: continue #list length<20,then the folder wont used for training
            else:
                WriteFileList(Dir,list,str(label),str(data_set))
                label=label+1
                print s
                if(label==data_set): break
    print label
print 'Write Output.txt Done!!!'
