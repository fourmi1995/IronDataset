from PIL import Image
import os
from math import sin

OrigRoot="/home/fourmi/桌面/黑色/"
ImgPath="Imgs_all/"
LabelPath="Labels_all/"
ImgFinal="RotatedImgs/"
LabelFinal="RotatedLabels/"

if not os.path.exists(ImgFinal):
    os.mkdir(ImgFinal)
if not os.path.exists(LabelFinal):
    os.mkdir(LabelFinal)

def rotate(Path,suffix_name,theta):

    for root,dirs,files in os.walk(Path,topdown=True):
        for filename in files:
            ImgPath = OrigRoot+root+'/'+filename
            if(suffix_name=='JPG'):
                savePath=OrigRoot+ImgFinal+filename[:-4]+'_'+str(theta)+'.JPG'
            if(suffix_name=='png'):
                savePath=OrigRoot+LabelFinal+filename[:-4]+'_'+str(theta)+'.png'
            with Image.open(ImgPath) as image:
                w, h = image.size
                x = y = 0
                x_c =int(x+w/2)
                y_c=int(y+h/2)
                out = image.rotate(theta)
                crop=out.crop((x_c,y_c,x_c+350,y_c+350))
                crop.save(savePath,quality=100)    



rotate(ImgPath,'JPG',45)
print('Rotate JPG for 45 done!!')
rotate(ImgPath,'JPG',135)
print('Rotate JPG for 135 done!!')
rotate(ImgPath,'JPG',225)
print('Rotate JPG for 225 done!!')
rotate(ImgPath,'JPG',315)
print('Rotate JPG for 315 done!!')
rotate(LabelPath,'png',45)
print('Rotate png for 45 done!!')
rotate(LabelPath,'png',135)
print('Rotate png for 135 done!!')
rotate(LabelPath,'png',225)
print('Rotate png for 225 done!!')
rotate(LabelPath,'png',315)
print('Rotate png for 315 done!!')

