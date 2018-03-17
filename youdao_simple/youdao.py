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


def fetch(query_str):
    '''
    use youdao api to get json result of translation
    '''
    print("查询单词：", query_str.strip())
    query = {
        'q': query_str.strip()
    }
    url = URL + urlencode(query)
    response = urlopen(url, timeout=3)
    html = response.read().decode("utf-8")
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


def parse(html):
    '''
    parse the json result to what user could read
    '''
    translation = json.loads(html)
    if translation.get('errorCode') == 0:
        if 'translation' in translation:
            print_translate(translation.get('translation'))
        if 'basic' in translation:
            print_basic(translation.get('basic'))
        if 'web' in translation:
            print_web(translation.get('web'))
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


def sanitize_arg(query_str):
    '''
    sanitize the argument first
    '''
    if hasattr(query_str, "decode"):
        result = query_str.decode("utf8")
        result = result.strip("'")
        result = result.strip('"')
        result = result.encode("utf-8")
    else:
        result = query_str.strip("'").strip('"')
    return result


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
        parse(youdao_json)
        print("<----------------------------------------------->")


if __name__ == '__main__':
    main()
