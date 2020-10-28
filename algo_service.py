# encoding:utf-8
# date:2020-10-26
# Author: X.L.Eric
# function: algo service

from flask import request, Flask, Response
import base64
import cv2
import numpy as np
import json
image_index = 0
app = Flask(__name__)

@app.route("/register", methods=['POST','GET'])
def get_frame():
    global image_index
    #解析图片数据
    img = base64.b64decode(str(request.form['image']))
    password = request.form["password"]
    user = request.form["user"]

    print("   user : {}, password : {}".format(user,password))

    image_data = np.fromstring(img, np.uint8)
    image_data = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    image_index += 1
    #------------------------ to do 算法解析



    cv2.imwrite('./service_get/example_{}.jpg'.format(image_index), image_data)
    print('{}) image_data shape : {} '.format(image_index,image_data.shape))

    dict_ = {
            "name":'test',
            }
    return Response(json.dumps(dict_),  mimetype='application/json')
if __name__ == "__main__":
    #多进程或多线程只能选择一个，不能同时开启
    # threaded=True
    # processes=True
    app.run(
        host = "localhost",
        port= 6666,
        debug = False,
        threaded = True,
        )
