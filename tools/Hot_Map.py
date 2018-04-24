import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
import numpy as np

def get_mask_image(img,img_x,img_y,kernel=8):
    mask_img=img.copy()
    cv.rectangle(mask_img,(img_x,img_y),(img_x+kernel,img_y+kernel),(0,0,0,),-1)
    return mask_img

def plot_hot_map(): #(x,y,v):
    x=[30.29459953,65.53179932,48.02519989,33.54930115,62.72990036]
    y=[112-51.69630051,112-51.69630051,112-71.73660278,112-92.3655014,112-92.20410156]
    #plt.imshow(z+10,cmap=cm.hot,norm=LogNorm())
    z=np.load('similar_pair_ct_1_Hot_map65_1.npy')
    plt.xlim(0,96)
    plt.ylim(0,112)

    plt.pcolor(z,cmap=plt.cm.Reds) #Greys)  #Reds
    plt.colorbar()
    plt.scatter(x,y,color='w',s=30)

    
    plt.show()
    

if __name__=='__main__':
    img = cv.imread(u"0-FaceId-0.jpg")
    kernel=15
    print img.shape
    plot_hot_map()
    
#    for img_y in range(0,len(img),kernel):
#        for img_x in range(0,len(img[0]),kernel):
#            mask_img=get_mask_image(img,img_x,img_y,kernel)
#            cv.imshow('test', mask_img)
#            cv.imwrite('maske_img.jpg',mask_img)
#            cv.waitKey()
    

