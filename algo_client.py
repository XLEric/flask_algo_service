# encoding:utf-8
# date:2020-10-26
# Author: X.L.Eric
# function: algo client

import requests
import base64
import os
import cv2
import json

if __name__ == "__main__":

    path = './images/'

    for file in os.listdir(path):
        img_path = path + file
        img_ = cv2.imread(img_path)

        img_str = cv2.imencode('.jpg', img_)[1].tobytes()  # 将图片编码成流数据，放到内存缓存中，然后转化成string格式
        #将图片数据转成base64格式
        img = base64.b64encode(img_str)

        params = {
            "image" : img,
            "password": 123456,
            "user" : 'eric',
            }

        # 如果需要在通过flask 在不同计算机进行通信， host 需要设置为 service ip v4
        host = "http://localhost:"
        port = "6666"
        request_url = host + port + "/register"

        r = requests.post(request_url, data=params)

        #------------------------ to do 算法结果解析
        data = r.json()
        print('data : ',data)
