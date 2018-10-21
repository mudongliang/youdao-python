#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Simple module to translate English to Chinse, Chinese to English
'''

# APP KEY    : 110b85528ad498df
# SECRET KEY : XS9nHguUbINnv7QFuXEmS1sHHa7VeyaK

from __future__ import print_function, unicode_literals
import json
import sys
import random
import hashlib


try:
    # compatible for python2
    from urllib import urlencode
    from urllib2 import urlopen
    from urllib2 import URLError
except ImportError:
    # compatible for python3
    from urllib.parse import urlencode
    from urllib.request import urlopen
    from urllib.error import URLError


URL = "https://openapi.youdao.com/api?"
APP_KEY = "110b85528ad498df"
SECRET_KEY = "XS9nHguUbINnv7QFuXEmS1sHHa7VeyaK"

def fetch(query_str):
    '''
    use youdao api to get json result of translation
    '''
    print("查询单词：", query_str.strip())

    html = ""
    salt = random.randint(1, 65536)

    if hasattr(query_str, "decode"):
        q = query_str.decode('UTF-8')
    else:
        q = query_str

    # generate signature
    string = APP_KEY+q+str(salt)+SECRET_KEY
    string = string.encode(encoding='UTF-8')
    sign = hashlib.md5(string).hexdigest()

    query = {
        'appKey': APP_KEY,
        'q': query_str,
        'from': "auto",
        'to': "auto",
        'salt': str(salt),
        'sign': sign
    }

    url = URL + urlencode(query)
    try:
        response = urlopen(url, timeout=3)
        html = response.read().decode("utf-8")
    except URLError as err:
        print(err.reason)

    return html

def print_basic(basic):
    '''
    print basic translation
    '''
    print("")
    print("有道词典-基本词典：")
    print("发音 [", basic.get("phonetic"), ']')
    if ("uk-phonetic" in basic) and ("us-phonetic" in basic):
        print("英式发音 [",
              basic.get("uk-phonetic"), "] \t",
              "美式发音 [",
              basic.get('us-phonetic'), ']')
    elif "uk-phonetic" in basic:
        print("英式发音 [", basic.get("uk-phonetic"), ']')
    elif "us-phonetic" in basic:
        print("美式发音 [", basic.get("us-phonetic"), ']')
    else:
        pass

    if "explains" in basic:
        basicexplains = basic.get("explains")
        for explain in basicexplains:
            print(explain)


def print_web(web):
    '''
    print web translation
    '''
    print("")
    print("有道词典-网络释义：")
    for explain in web:
        value = ""
        for exp in explain["value"]:
            value += exp
            value += " "
        print(explain["key"], " : ", value)


def print_translate(translate):
    '''
    print translation
    '''
    print("有道翻译：", end='')
    for trans in translate:
        print(trans, end='')
    print("")


def print_dict(ldict, webdict):
    '''
    print dictionary URL
    '''
    print("")
    print("有道翻译-词典URL：")
    print("词典URL:", ldict["url"])
    print("网络词典URL:", webdict["url"])

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

def parse(html):
    '''
    parse the json result to what user could read
    '''
    translation = json.loads(html)
    if translation.get('errorCode') == '0':
        #print(translation.get('query')) 
        if 'translation' in translation:
            print_translate(translation.get('translation'))
        if 'basic' in translation:
            print_basic(translation.get('basic'))
        if 'web' in translation:
            print_web(translation.get('web'))
        #if 'dict' in translation and 'webdict' in translation:
        #    print_dict(translation.get('dict'), translation.get('webdict'))
    else:
        print_err_message(translation.get('errorCode'))


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
        youdao_json = fetch(sanitize_arg(argument))
        if youdao_json:
            parse(youdao_json)
        print("<----------------------------------------------->")


if __name__ == '__main__':
    main()
