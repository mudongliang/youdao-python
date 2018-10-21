#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Simple module to pronunce English words
'''

# APP KEY    : 110b85528ad498df
# SECRET KEY : XS9nHguUbINnv7QFuXEmS1sHHa7VeyaK

from __future__ import print_function, unicode_literals
import sys
import time
import random
import hashlib
import vlc
from termcolor import colored
import requests

URL = "https://openapi.youdao.com/ttsapi?"
APP_KEY = "110b85528ad498df"
SECRET_KEY = "XS9nHguUbINnv7QFuXEmS1sHHa7VeyaK"
TEMP_MP3 = "/tmp/temp.mp3"

def fetch(query_str, lang="en"):
    '''
    use youdao TTS api to get pronounction
    '''
    salt = random.randint(1, 65536)

    if hasattr(query_str, "decode"):
        query = query_str.decode('UTF-8')
    else:
        query = query_str

    desc = colored("查询单词："+query, "red", attrs=['bold'])
    print(desc)

    # generate signature
    string = APP_KEY+query+str(salt)+SECRET_KEY
    string = string.encode(encoding='UTF-8')
    sign = hashlib.md5(string).hexdigest()

    args = {
        'appKey': APP_KEY,
        'langType': lang,
        'q': query,
        'from': "auto",
        'to': "auto",
        'salt': str(salt),
        'sign': sign
    }

    try:
        response = requests.post(URL, args)
    except requests.exceptions.RequestException as ex:
        print(ex)
        exit(0)

    return response


def print_err_message(err_code):
    '''
    get error message from Error Code
    '''
    err_message = {
        '101':"缺少必填的参数，出现这个情况还可能是et的值和实际加密方式不对应",
        '102':"不支持的语言类型",
        '103':"翻译文本过长",
        '104':"不支持的API类型",
        '105':"不支持的签名类型",
        '106':"不支持的响应类型",
        '107':"不支持的传输加密类型",
        '108':"appKey无效，注册账号， 登录后台创建应用和实例并完成绑定， 可获得应用ID和密钥等信息，其中应用ID就是appKey（ 注意不是应用密钥）",
        '109':"batchLog格式不正确",
        '110':"无相关服务的有效实例",
        '111':"开发者账号无效",
        '113':"q不能为空",
        '201':"解密失败，可能为DES,BASE64,URLDecode的错误",
        '202':"签名检验失败",
        '203':"访问IP地址不在可访问IP列表",
        '205':"请求的接口与选择的接入方式不一致",
        '301':"辞典查询失败",
        '302':"翻译查询失败",
        '303':"服务端的其它异常",
        '401':"账户已经欠费",
        '411':"访问频率受限,请稍后访问",
        '2005':"ext参数不对",
        '2006':"不支持的voice"
    }
    if err_code in err_message:
        print(err_message[err_code])


def save(mp3, content):
    '''
    save mp3 file in the /tmp/temp.mp3
    '''
    #print("Save MP3 File")
    file_desc = open(mp3, "wb")
    file_desc.write(content)
    file_desc.close()

def play(mp3, period=1):
    '''
    play mp3
    '''
    #print("Play MP3 File")
    player = vlc.MediaPlayer(mp3)
    player.play()
    time.sleep(period)


def sanitize_arg(query_str):
    '''
    sanitize the argument first
    '''
    if hasattr(query_str, "decode"):
        result = query_str.decode("utf-8")
        result = result.strip("'")
        result = result.strip('"')
        result = result.encode("utf-8")
    else:
        result = query_str.strip("'").strip('"')
    return result.strip()


def main():
    '''
    parse arguments to translate
    '''
    if len(sys.argv) == 1:
        print('No word to translate')
        exit(0)
    for argument in sys.argv[1:]:
        print("<----------------------------------------------->")
        response = fetch(sanitize_arg(argument))
        content_type = response.headers['content-type']
        if content_type == "audio/mp3":
            save(TEMP_MP3, response.content)
            play(TEMP_MP3)
        print("<----------------------------------------------->")


if __name__ == '__main__':
    main()
