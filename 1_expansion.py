from img_logging import Logger
from PIL import Image
import os

# 声明日志
log = Logger('expansion.py')
logger = log.getlog()


class ImgPre:
    def __init__(self, rootPath, export_path_base,number,rootLabelPath,export_path_base_label):
        self.rootPath = rootPath  # 图像完整路径
        self.export_path_base = export_path_base
        self.number=number
        self.rootLabelPath=rootLabelPath
        self.export_path_base_label=export_path_base_label
        print(self.rootPath)
        print(self.export_path_base)

        # 创建输出根目录
        try:
            if not os.path.exists(export_path_base):
                os.mkdir(export_path_base)
            if not os.path.exists(export_path_base_label):
                os.mkdir(export_path_base_label)
        except Exception as e:
            logger.error(e)
        logger.info('ImgPre: %s', rootPath)

    def get_savename(self, operate,number):
        """
        :param export_path_base: 图像输出路径
        :param operate: 脸部区域名

        :return: 返回图像存储名
        """
        try:
            import time
            # 获取时间戳，用于区分图像
            now = time.time()
            tail_time = str(round(now * 1000000))[-4:]  # 时间戳尾数
            head_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            # 时间标签
            label = str(head_time + tail_time)

            # 输出文件夹
            export_path_base = self.export_path_base
            export_path_label_base=self.export_path_base_label
            # 子文件夹以“操作operate”命名
            out_path = export_path_base + operate
            out_label_path=export_path_label_base+operate
            print("***************************************")
            print('out_label_path:',out_label_path)
            print("***************************************")
            # 创建子文件夹
            if not os.path.exists(out_path):
                os.mkdir(out_path)
            if not os.path.exists(out_label_path):
                os.mkdir(out_label_path)

            # 存储完整路径
            savename = out_path + '/' + operate + '_' + str(number)+ ".JPG"
            label_savename=out_label_path+ '/' + operate + '_'+str(number)+ ".png"

            # 日志
            logger.info('save:%s', savename)
            logger.info('save:%s', label_savename)
            return savename,label_savename

        except Exception as e:
            logger.error('get_savename ERROR')
            logger.error(e)

    def lightness(self, light):
        """改变图像亮度.
        推荐值：
            0.87，1.07
        明亮程度
            darker < 1.0 <lighter
        """
        try:
            operate = 'lightness_' + str(light)
            # 图像完整路径
            rootPath = self.rootPath
            LabelRootPath=self.rootLabelPath

            with Image.open(rootPath) as image:
                # 图像左右翻转
                out = image.point(lambda p: p * light)
                # 重命名
                savename, _ = self.get_savename(operate,self.number)
                # 图像存储
                out.save(savename)
            with Image.open(LabelRootPath) as label:
                _,savename = self.get_savename(operate,self.number)
                label.save(savename)
            # 日志
            # logger.info(operate)
        except Exception as e:
            logger.error('ERROR %s', operate)
            logger.error(e)

    def transpose(self):
        """图像左右翻转操作."""
        try:
            operate = 'transpose_L_R'
            operate1 = 'transpose_U_D'
            operate2 = 'transpose_90'
            operate3 = 'transpose_180'
            operate4 = 'transpose_270'
            # 图像完整路径
            rootPath = self.rootPath
            LabelRootPath=self.rootLabelPath
            with Image.open(rootPath) as image:
                # 图像左右翻转
                out = image.transpose(Image.FLIP_LEFT_RIGHT)
                out1 = image.transpose(Image.FLIP_TOP_BOTTOM)
                out2 = image.transpose(Image.ROTATE_90)
                out3 = image.transpose(Image.ROTATE_180)
                out4 = image.transpose(Image.ROTATE_270)
                # 重命名
                savename,_ = self.get_savename(operate,self.number)
                savename1,_ = self.get_savename(operate1,self.number)
                savename2,_ = self.get_savename(operate2,self.number)
                savename3,_ = self.get_savename(operate3,self.number)
                savename4,_ = self.get_savename(operate4,self.number)
                # 图像存储
                out.save(savename, quality=100)  # quality=100
                out1.save(savename1,quality=100)
                out2.save(savename2,quality=100)
                out3.save(savename3,quality=100)
                out4.save(savename4,quality=100)
            with Image.open(LabelRootPath) as label:
                # 图像左右翻转
                out = label.transpose(Image.FLIP_LEFT_RIGHT)
                out1 = label.transpose(Image.FLIP_TOP_BOTTOM)
                out2 = label.transpose(Image.ROTATE_90)
                out3 = label.transpose(Image.ROTATE_180)
                out4 = label.transpose(Image.ROTATE_270)
                # 重命名
                _,savename = self.get_savename(operate,self.number)
                _,savename1 = self.get_savename(operate1,self.number)
                _,savename2 = self.get_savename(operate2,self.number)
                _,savename3 = self.get_savename(operate3,self.number)
                _,savename4 = self.get_savename(operate4,self.number)
                # 图像存储
                out.save(savename, quality=100)  # quality=100
                out1.save(savename1,quality=100)
                out2.save(savename2,quality=100)
                out3.save(savename3,quality=100)
                out4.save(savename4,quality=100)

            # 日志
            # logger.info(operate)
        except Exception as e:
            logger.error('ERROR %s', operate)
            logger.error(e)

    def deform(self):
        """图像拉伸."""
        try:
            operate = 'deform'
            # 图像完整路径
            rootPath = self.rootPath
            LabelRootPath=self.rootLabelPath
            with Image.open(rootPath) as image:
                w, h = image.size
                w = int(w)
                h = int(h)
                # 拉伸成宽为w的正方形
                out_ww = image.resize((int(w), int(w)))
                savename, _ = self.get_savename(operate + '_ww',self.number)
                out_ww.save(savename, quality=100)
                # 拉伸成宽为h的正方形
                out_ww = image.resize((int(h), int(h)))
                savename, _ = self.get_savename(operate + '_hh',self.number)
                out_ww.save(savename, quality=100)
            with Image.open(LabelRootPath) as label:
                w, h = label.size
                w = int(w)
                h = int(h)
                out_ww = label.resize((int(w),int(w)))
                _, savename = self.get_savename(operate + '_ww',self.number)
                out_ww.save(savename, quality=100)
                out_ww = label.resize((int(h),int(h)))
                _, savename = self.get_savename(operate + '_hh',self.number)
                out_ww.save(savename,quality=100)
            # 日志
            # logger.info(operate)
        except Exception as e:
            logger.error('ERROR %s', operate)
            logger.error(e)


    def crop(self):
        """提取四个角落和中心区域."""
        try:
            operate = 'crop'
            # 图像完整路径
            rootPath = self.rootPath
            LabelRootPath=self.rootLabelPath
            with Image.open(rootPath) as image:
                w, h = image.size
                # 切割后尺寸
                scale = 0.875
                # 切割后长宽
                ww = int(w * scale)
                hh = int(h * scale)
                # 图像起点，左上角坐标
                x = y = 0

                # 切割左上角
                x_lu = x
                y_lu = y
                out_lu = image.crop((x_lu, y_lu, ww, hh))
                savename, _ = self.get_savename(operate + '_lu',self.number)
                out_lu.save(savename, quality=100)
                # logger.info(operate + '_lu')

                # 切割左下角
                x_ld = int(x)
                y_ld = int(y + (h - hh))
                out_ld = image.crop((x_ld, y_ld, ww, hh))
                savename, _ = self.get_savename(operate + '_ld',self.number)
                out_ld.save(savename, quality=100)
                # logger.info(operate + '_ld')

                # 切割右上角
                x_ru = int(x + (w - ww))
                y_ru = int(y)
                out_ru = image.crop((x_ru, y_ru, w, hh))
                savename, _ = self.get_savename(operate + '_ru',self.number)
                out_ru.save(savename, quality=100)
                # logger.info(operate + '_ru')

                # 切割右下角
                x_rd = int(x + (w - ww))
                y_rd = int(y + (h - hh))
                out_rd = image.crop((x_rd, y_rd, w, h))
                savename, _ = self.get_savename(operate + '_rd',self.number)
                out_rd.save(savename, quality=100)
                # logger.info(operate + '_rd')

                # 切割中心
                x_c = int(x + (w - ww) / 2)
                y_c = int(y + (h - hh) / 2)
                out_c = image.crop((x_c, y_c, ww, hh))
                savename, _ = self.get_savename(operate + '_c',self.number)
                out_c.save(savename, quality=100)
                # logger.info('提取中心')
            with Image.open(LabelRootPath) as label:
                w, h = label.size
                scale = 0.875
                ww = int(w * scale)
                hh = int(h * scale)

                x = y =0

                x_lu = x
                y_lu = y
                out_lu = label.crop((x_lu,y_lu,ww,hh))
                _, savename = self.get_savename(operate + '_lu', self.number)
                out_lu.save(savename, quality=100)

                x_ld = int(x)
                y_ld = int(y + (h - hh))
                out_ld = label.crop((x_ld,y_ld,ww,hh))
                _, savename = self.get_savename(operate + '_ld',self.number)
                out_ld.save(savename, quality=100)

                x_ru = int(x+(w-ww))
                y_ru = int(y)

                out_ru = label.crop((x_ru,y_ru,w,hh))
                _,savename = self.get_savename(operate + '_ru',self.number)
                out_ru.save(savename,quality=100)

                x_rd = int(x+(w-ww))
                y_rd = int(y+(h-hh))
                out_rd = label.crop((x_rd,y_rd,w,h))
                _,savename = self.get_savename(operate + '_rd',self.number)
                out_rd.save(savename,quality=100)

                x_c = int(x+(w-ww)/2)
                y_c = int(y+(h-hh)/2)
                out_c = label.crop((x_c,y_c,ww,hh))
                _,savename = self.get_savename(operate + '_c',self.number)
                out_c.save(savename,quality=100)




        except Exception as e:
            logger.error('ERROR %s', operate)
            logger.error(e)

def test(number):
    # 源地址和输出地址
    rootPath = './images/'+str(number)+'.JPG'
    rootLabelPath='./labels/'+str(number)+'.png'
    export_path_base = './images_expansion/'+str(number)+'/'
    export_path_base_label = './labels_expansion/'+str(number)+'/'

    # 声明类对象
    imgPre = ImgPre(rootPath, export_path_base,number,rootLabelPath,export_path_base_label)
    imgPre.deform()
    imgPre.transpose()
    imgPre.crop()
    imgPre.lightness(1.07)
    imgPre.lightness(0.87)
    imgPre.lightness(0.80)
    imgPre.lightness(1.20)
    

if __name__ == '__main__':
    import datetime
    print('start...')
    # 计时
    start_time = datetime.datetime.now()
    for i in range(25):
        print('i:----------------------------------------------',i)
        test(i+1)

    end_time = datetime.datetime.now()
    time_consume = (end_time - start_time).microseconds / 1000000

    logger.info('start_time: %s', start_time)
    logger.info('end_time: %s', end_time)
    logger.info('time_consume: %s(s)', time_consume)  # 0.280654(s)

    logger.info('main finish')
