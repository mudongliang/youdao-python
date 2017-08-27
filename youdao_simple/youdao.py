#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
simple module to translate English to Chinse, Chinese to English
'''

# API key：701380394
# keyfrom：youdao-python

from __future__ import print_function, unicode_literals
import json
import sys


try:
    # compatible for python2
    from urllib import urlencode
    from urllib2 import urlopen
except ImportError:
    # compatible for python3
    from urllib.parse import urlencode
    from urllib.request import urlopen


URL = "http://fanyi.youdao.com/openapi.do?" + \
      "keyfrom=youdao-python&key=701380394" + \
      "&type=data&doctype=json&version=1.1&"

def fetch(query_str=''):
    '''
    use youdao api to get json result of translation
    '''
    query_str = query_str.strip("'").strip('"').strip()

    print(query_str)
    query = {
        'q': query_str
    }
    url = URL + urlencode(query)
    response = urlopen(url, timeout=3)
    html = response.read().decode('utf-8')
    return html


def parse(html):
    '''
    parse the json result to what user could read
    '''
    translation = json.loads(html)
    if translation.get('errorCode') == 0:
        print("有道翻译 : ")
        for trans in translation.get("translation"):
            print(trans)
        print("")
        print("有道词典-基本词典 : ")
        basicexplains = translation.get('basic').get('explains')
        print("英式发音 [", translation.get("basic").get("uk-phonetic"), "] \t"+
              "美式发音 [", translation.get("basic").get("us-phonetic"), "]")
        for explain in basicexplains:
            print(explain)
        print("")
        print("有道词典-网络释义 : ")
        webexplains = translation.get("web")
        for explain in webexplains:
            value = ""
            for exp in explain["value"]:
                value += exp
                value += " "
            print(explain["key"], " : ", value)
    elif translation.get('errorCode') == 20:
        print('要翻译的文本过长')
    elif translation.get('errorCode') == 30:
        print('无法进行有效的翻译')
    elif translation.get('errorCode') == 40:
        print('不支持的语言类型')
    elif translation.get('errorCode') == 50:
        print('无效的key')
    elif translation.get('errorCode') == 60:
        print('无词典结果，仅在获取词典结果生效')
    else:
        print('翻译出错，请输入合法单词')


def main():
    '''
    parse arguments to translate
    '''
    if len(sys.argv) == 1:
        print("No word to translate")
        exit(0)
    for argument in sys.argv[1:]:
        parse(fetch(argument))

if __name__ == '__main__':
    main()
