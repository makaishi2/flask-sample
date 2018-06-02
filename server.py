#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib3, requests, json
import os
from os.path import join, dirname
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def top():
    name = "Top"
    return render_template('sample.html', title='Flask Sample Web', name=name)

# 「送信」ボタンが押された時の処理
@app.route('/send', methods=['POST'])
def send():
    # パラメータの受け取り
    req_json = request.json
    arg1 = req_json['ARG1']
    arg2 = req_json['ARG2']

    # ダミーのサーバー処理
    sum = arg1 + arg2
    print(arg1, arg2, sum)

    # 戻り用変数の定義
    ret = {'ARG1': arg1, 'ARG2': arg2, 'SUM': sum}
    
    # json.dumps の結果を戻り値とする
    return(json.dumps(ret))

@app.route('/favicon.ico')
def favicon():
   return ""

port = os.getenv('VCAP_APP_PORT', '8000')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)