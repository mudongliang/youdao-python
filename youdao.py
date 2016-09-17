#!/usr/bin/env python
# -*- coding:utf-8 -*-

# API key：701380394
# keyfrom：youdao-python

import json
import sys

try:        # python3
    from urllib.parse import urlparse, quote, urlencode, unquote
    from urllib.request import urlopen
except:     # python2
    from urllib import urlencode, quote, unquote
    from urllib2 import urlopen


def fetch(query_str=''):
    query_str = query_str.strip("'").strip('"').strip()

    print(query_str)
    query = {
        'q': query_str
    }
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=youdao-python&key=701380394&type=data&doctype=json&version=1.1&' + urlencode(query)
    response = urlopen(url, timeout=3)
    html = response.read().decode('utf-8')
    return html


def parse(html):
    d = json.loads(html)
    try:
        if d.get('errorCode') == 0 :
            explains = d.get('basic').get('explains')
            for explain in explains:
                print(explain)
        elif d.get('errorCode' == 20) :
            print('要翻译的文本过长')
        elif d.get('errorCode' == 30) :
            print('无法进行有效的翻译')
        elif d.get('errorCode' == 40) :
            print('不支持的语言类型')
        elif d.get('errorCode' == 50) :
            print('无效的key')
        else :
            print('无词典结果，仅在获取词典结果生效')
    except:
        print('翻译出错，请输入合法单词')


def main():
    if (len(sys.argv) == 1):
        print("No word to translate")
        exit(0)
    for argument in sys.argv[1:]:
        parse(fetch(argument))
        print("")

if __name__ == '__main__':
    main()
