import keras as k
from keras.models import load_model
import numpy as np
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
from keras.applications import *
import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
class flower_model:
    def __init__(self):
        self.model =load_model(os.path.join(os.getcwd(),"pic","model","Best_Model.h5"))
        # 相对路径改为绝对路径
    def predict_fun(self,dirs):
        img =image.load_img(dirs, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis=0)
        pre = sorted(self.model.predict(x).reshape(-1))[::-1][:10]
        y = self.model.predict(x).reshape(-1).argsort()[::-1][:10]##将预测矩阵降为向量，再argsort输出从小到大排序索引，反转，取前值排名前十的索引
#         dict_ = dict(zip(y,pre))
        label= [self.data_select(i)[0] for i in y]
        self.dict_= dict(zip(label,pre))
        return self.dict_
    #标签映射
    def data_select(self,num):
        import pandas as pd
        # path =r"C:\Users\Administrator\Desktop\数据分析平台\flower_model\flowers_label.csv"
        path = os.path.join(os.getcwd(), "pic", "model", "flowers_label.csv")
        data = pd.read_csv(path)
        self.da = data.iloc[data.iloc[:,0].values==num,1].values
        return self.da
# if __name__=='__main__':
#     f = flower_model()
#     dirs = r".\327.jpeg"
#     dict_=f.predict_fun(dirs)
#     print(dict_)