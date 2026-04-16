#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app.py
# @Software: PyCharm
# @define  : function

import re
import json
import base64
import numpy as np
import tensorflow.keras as keras
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# 使用 redis 统计总访问次数，今日访问次数from redis_util import get_today, get_visit_num_all, get_visit_num_today, inc_visit_num

app = Flask(__name__)

model_file = './model/model.h5'
global model
model = keras.models.load_model(model_file)

@app.route('/')
def index():
    # inc_visit_num()
    response = {
        'code': 0,
        'visits_all': 10086,              # 假数据：总访问次数
        'visits_today': 123,              # 假数据：今日访问次数
        'today': '2025-04-05'             # 假数据：今日日期
    }
    return render_template("index.html", **response)  # 如果没有使用 redis 统计访问次数功能，请使用index.html

@app.route('/predict/', methods=['Get', 'POST'])
def preditc():
    # inc_visit_num()  # 每访问一次，增加访问次数
    parseImage(request.get_data())
    img = img_to_array(load_img('output.png', target_size=(28, 28), color_mode="grayscale")) / 255.
    img = np.expand_dims(img, axis=0)
    code = model.predict_classes(img)[0]
    response = {
        'code': 0,
        'visits_all': 10086,              # 假数据：总访问次数
        'visits_today': 123,              # 假数据：今日访问次数
        'today': '2025-04-05'             # 假数据：今日日期
    }
    print(response)
    return jsonify(int(code))

'''
def get_visit_info(code=0):
    response = {}
    response['code'] = code
    response['visits_all'] = get_visit_num_all()
    response['visits_today'] = get_visit_num_today()
    response['today'] = get_today()
    return response
'''
def parseImage(imgData):
    imgStr = re.search(b'base64,(.*)', imgData).group(1)
    with open('./output.png', 'wb') as output:
        output.write(base64.decodebytes(imgStr))
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3335)