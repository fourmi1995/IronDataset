import os
from PIL import Image

OrigRoot="/home/fourmi/桌面/黑色/"

ImgRootPath="images_expansion"
LabelRootPath="labels_expansion"
ImgPath="Imgs_all/"
LabelPath="Labels_all/"

if not os.path.exists(ImgPath):
    os.mkdir(ImgPath)
if not os.path.exists(LabelPath):
    os.mkdir(LabelPath)
def extract(Path,suffix_name):
    index=1
    for root,dirs,files in os.walk(Path,topdown=False):
        for filename in files:
            Imgpath=OrigRoot+root+'/'+filename    
            if(suffix_name=='JPG'):
                savePath=OrigRoot+ImgPath+str(index)+'.JPG'
            if(suffix_name=='png'):
                savePath=OrigRoot+LabelPath+str(index)+'.png'
            with Image.open(Imgpath) as image:
                image.save(savePath)
            index=index+1

extract(ImgRootPath,'JPG')
print("extract all images done!!")
extract(LabelRootPath,'png')
print("extract all lables done!!")
