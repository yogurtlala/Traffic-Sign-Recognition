import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from skimage.feature import blob_dog, blob_log, blob_doh
import imutils
import argparse
import os
import math
import random
import pandas as pd
import skimage.data
import skimage.transform
# import tensorflow as tf
import matplotlib.pyplot as plt
# from tensorflow import keras
from sklearn import metrics
import joblib
from skimage.feature import hog
from skimage import io, transform
def get_result():
    SIGNS = ["hhh",
            "SPEED LIMIT 5",
            "DO NOT GO STRAIGHT",
            "DO NOT TURN LEFT",
            "DO NOT TURN LEFT AND TURN RIGHT",
            "DO NOT TURN RIGHT",
            "DO NOT OVERTAKE",
            "NO CARS",
            "DO NOT HONK",
            "NO STOPPING",
            "I DONT KNOW"
            ]

    def constrastLimit(image): # 输入图像
        img_hist_equalized = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb) # YCrCb是BGR颜色空间的一种解码方式
        channels = cv2.split(img_hist_equalized) # 拆分图像通道 B/G/R
        channels[0] = cv2.equalizeHist(channels[0]) # 直方图均衡化
        img_hist_equalized = cv2.merge(channels) # 合并图像通道
        img_hist_equalized = cv2.cvtColor(img_hist_equalized, cv2.COLOR_YCrCb2BGR) # 转为BGR格式
        return img_hist_equalized # 输出图像

    def LaplacianOfGaussian(image): # 输入图像
        LoG_image = cv2.GaussianBlur(image, (3,3), 0) # 高斯滤波 减噪
        gray = cv2.cvtColor(LoG_image, cv2.COLOR_BGR2GRAY) # 转为灰度图
        LoG_image = cv2.Laplacian(gray, cv2.CV_8U,3,3,2) # Laplacian算子 检测边缘
        LoG_image = cv2.convertScaleAbs(LoG_image) # 实现将原图片转换为uint8类型
        return LoG_image # 输出图像

    def binarization(image): # 输入图像
        thresh = cv2.threshold(image,32,255,cv2.THRESH_BINARY)[1] # 二值化 灰度图像转为二值图像
        return thresh # 输出二值图像

    def preprocess_image(image): # 输入图像 预处理
        image = constrastLimit(image)
        image = LaplacianOfGaussian(image)
        image = binarization(image)
        return image # 输出图像

    def removeSmallComponents(image, threshold): # 输入图像和阈值
        nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8) # 查找所有连接的部分
        # 返回值： nb_components 连通区域数量 output 与image大小相同的矩形 每一个连通区域有一个唯一标识
        # stats 包含五个参数x y h w s，分别对应每一个连通区域的外接矩形的起始坐标
        # centroids 连通区域的质心
        sizes = stats[1:, -1]; nb_components = nb_components - 1
        img2 = np.zeros((output.shape),dtype = np.uint8)
        
        for i in range(0, nb_components): # 对于每个部分 仅当高于阈值才保留
            if sizes[i] >= threshold:
                img2[output == i + 1] = 255
        return img2 # 输出图像

    def findContour(image): # 输入图像
        cnts, h = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 查找轮廓
        return cnts # 返回list list中的每一个元素都是一个轮廓

    def contourIsSign(perimeter, centroid, threshold): # 参数：周长 圆心 阈值
        result = []
        for p in perimeter: # 算出每个点离质心的距离 存入result
            p = p[0]
            distance = sqrt((p[0] - centroid[0])**2 + (p[1] - centroid[1])**2)
            result.append(distance)
            
        max_value = max(result) # 找到最大距离
        signature = [float(dist) / max_value for dist in result ] # 
        temp = sum((1 - s) for s in signature)
        temp = temp / len(signature)
        
        if temp < threshold: 
            return True, max_value + 2
        else:                
            return False, max_value + 2

    def cropSign(image, coordinate): # 输入图像 坐标
        width = image.shape[1] # 宽
        height = image.shape[0] # 高
        top = max([int(coordinate[0][1]), 0])
        bottom = min([int(coordinate[1][1]), height-1])
        left = max([int(coordinate[0][0]), 0])
        right = min([int(coordinate[1][0]), width-1])
        return image[top:bottom,left:right] # 裁剪 输出裁剪后的图像

    def findLargestSign(image, contours, threshold, distance_theshold): # 输入图像 轮廓 阈值 距离阈值
        max_distance = 0
        coordinate = None
        sign = None
        for c in contours: # 遍历轮廓
            M = cv2.moments(c)
            if cv2.contourArea(c) == 0:
                continue
    #         if M["m00"] == 0:
    #             continue
            # M["m00"]表示轮廓面积 
            cX = int(M["m10"] / M["m00"]) # 质心 x
            cY = int(M["m01"] / M["m00"]) # 质心 y
            is_sign, distance = contourIsSign(c, [cX, cY], 1-threshold)
            if is_sign and distance > max_distance and distance > distance_theshold:
                max_distance = distance # 更新最大距离
                coordinate = np.reshape(c, [-1,2])
                left, top = np.amin(coordinate, axis=0)
                right, bottom = np.amax(coordinate, axis = 0)
                coordinate = [(left-2,top-2),(right+3,bottom+1)]
                sign = cropSign(image,coordinate)
        return sign, coordinate # 返回裁剪过后的图像

    def remove_other_color(img):
        frame = cv2.GaussianBlur(img, (3,3), 0) 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([100,128,0]) # 蓝色
        upper_blue = np.array([215,255,255])
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        lower_white = np.array([0,0,128], dtype=np.uint8)
        upper_white = np.array([255,255,255], dtype=np.uint8)
        mask_white = cv2.inRange(hsv, lower_white, upper_white)
        lower_black = np.array([0,0,0], dtype=np.uint8)
        upper_black = np.array([170,150,50], dtype=np.uint8)
        mask_black = cv2.inRange(hsv, lower_black, upper_black)
        mask_1 = cv2.bitwise_or(mask_blue, mask_white)
        mask = cv2.bitwise_or(mask_1, mask_black)
        return mask

    def localization(image, current_sign_type):
        original_image = image.copy()
        binary_image = preprocess_image(image)
        binary_image = removeSmallComponents(binary_image, 300)
        binary_image = cv2.bitwise_and(binary_image,binary_image, mask=remove_other_color(image))
        contours = findContour(binary_image)
        sign, coordinate = findLargestSign(original_image, contours, 0.65, 15)
        
        text = ""
        sign_type = -1
        i = 0
        new_model = joblib.load("my_model_SVM.m")
        
        if sign is not None:
            sign = cv2.cvtColor(sign, cv2.COLOR_BGR2GRAY) 
            sign = transform.resize(sign, (128, 128))
            feature = hog(sign, orientations=8, pixels_per_cell=(10, 10),
                    cells_per_block=(1, 1), visualize=False, multichannel=False)
            feature = feature.reshape(1, -1)
            y_pred = new_model.predict(feature)
            y_pred = y_pred[0]
            print(f'sign_type:{y_pred}')
            
            sign_type = y_pred

    #         sign_type = sign_type if sign_type <= 8 else 8
            text = SIGNS[sign_type]

        if sign_type > 0 and sign_type != current_sign_type: 
            cv2.rectangle(original_image, coordinate[0],coordinate[1], (245,255,0), 5)
            font = cv2.FONT_HERSHEY_PLAIN # 字体
            cv2.putText(original_image,text,(coordinate[0][0], coordinate[0][1] -8), font, 2,(245,255,0),5,cv2.LINE_4)
        return coordinate, original_image, sign_type, text

    vidcap = cv2.VideoCapture('video_test.MP4') # 视频文件
    fps = vidcap.get(cv2.CAP_PROP_FPS) # 帧速率
    width = int(vidcap.get(3))  # 帧的宽度
    height = int(vidcap.get(4)) # 帧的高度
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # 要保存视频的编码方式
    # out = cv2.VideoWriter('C:\\Users\\lenovo\\Desktop\\output2.avi',fourcc, fps , (640,800)) # 写视频
    out = cv2.VideoWriter('output6.avi',fourcc, fps, (width, height)) # 写视频

    termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    roiBox = None
    roiHist = None
    success = True
    count = 0
    current_sign = None
    current_text = ""
    current_size = 0
    sign_count = 0
    coordinates = []
    position = []

    while True:
        
        success,frame = vidcap.read() # 按帧读取视频 
        # 第一个返回值为布尔值 正确读取为True 读到结尾为False 第二个返回值为每一帧的图像/三维矩阵
        if not success: # 如果读到视频结尾
            print("FINISHED") # 输出FINISHED
            break # 跳出循环
            
        frame = cv2.resize(frame, (width,height))

        print("Frame:{}".format(count)) # 第几帧
        coordinate, image, sign_type, text = localization(frame, current_sign)
        
    #     if coordinate is not None:
    #         cv2.rectangle(image, coordinate[0],coordinate[1], (255, 255, 255), 1)
    #     print("Sign:{}".format(sign_type))
        
        if sign_type >= 0 and (not current_sign or sign_type != current_sign):
            current_sign = sign_type # 更新当前sign_type
            current_text = text
            top = int(coordinate[0][1]*1.05)
            left = int(coordinate[0][0]*1.05)
            bottom = int(coordinate[1][1]*0.95)
            right = int(coordinate[1][0]*0.95)

            position = [count, sign_type, coordinate[0][0], coordinate[0][1], coordinate[1][0], coordinate[1][1]]
            cv2.rectangle(image, coordinate[0],coordinate[1], (245,255,0), 5) # ？？？
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(image,text,(coordinate[0][0], coordinate[0][1] -15), font, 2,(245,255,0),5,cv2.LINE_4)

            tl = [left, top]
            br = [right,bottom]
            
            current_size = math.sqrt(math.pow((tl[0]-br[0]),2) + math.pow((tl[1]-br[1]),2)) # 对角线长
            
            
            roi = frame[tl[1]:br[1], tl[0]:br[0]] # 裁剪下的图片
            print(type(roi))
            if roi is not None:
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV) # HSV
            

                roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180]) # 直方图
                roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
                roiBox = (tl[0], tl[1], br[0], br[1])

        elif current_sign:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1) # 反向投影

            (r, roiBox) = cv2.CamShift(backProj, roiBox, termination) # 目标跟踪
            pts = np.int0(cv2.boxPoints(r))
            s = pts.sum(axis = 1)
            tl = pts[np.argmin(s)]
            br = pts[np.argmax(s)]
            size = math.sqrt(pow((tl[0]-br[0]),2) + pow((tl[1]-br[1]),2))

            if  current_size < 1 or size < 1 or size / current_size > 30 or math.fabs((tl[0]-br[0])/(tl[1]-br[1])) > 2 or math.fabs((tl[0]-br[0])/(tl[1]-br[1])) < 0.5:
                current_sign = None
                print("Stop tracking")
            else:
                current_size = size

            if sign_type > 0:
                top = int(coordinate[0][1])
                left = int(coordinate[0][0])
                bottom = int(coordinate[1][1])
                right = int(coordinate[1][0])

                cv2.rectangle(image, coordinate[0],coordinate[1], (245,255,0), 5)
                font = cv2.FONT_HERSHEY_PLAIN
                cv2.putText(image,text,(coordinate[0][0], coordinate[0][1] -15), font, 2,(245,255,0),5,cv2.LINE_4)
                
            elif current_sign:
                cv2.rectangle(image, (tl[0], tl[1]),(br[0], br[1]), (245,255,0), 5)
                font = cv2.FONT_HERSHEY_PLAIN
                cv2.putText(image,current_text,(tl[0], tl[1] -15), font, 2,(245,255,0),5,cv2.LINE_4)

        if current_sign:
            sign_count += 1

        count = count + 1
        out.write(image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    print("Finish {} frames".format(count))
    