# youdao-python
Youdao dictionary implemented in python

## Install

### pip

```
sudo pip install youdao_simple
```

### setup.py

```sh
$ git clone https://github.com/mudongliang/youdao-python
$ cd youdao-python
$ sudo python setup.py install
```

## Usage

```sh
$ youdao
No word to translate
```

```sh
$ youdao hello
<----------------------------------------------->
查询单词： hello
有道翻译：你好

有道词典-基本词典：
发音 [ həˈləʊ ]
英式发音 [ həˈləʊ ] 	 美式发音 [ helˈō ]
int. 喂；哈罗
n. 表示问候， 惊奇或唤起注意时的用语
n. (Hello)人名；(法)埃洛

有道词典-网络释义：
Hello  :  你好 您好 哈啰 喂 
Hello Kitty  :  凯蒂猫 昵称 匿称 最想当的商品代言人 
Hello Bebe  :  哈乐哈乐 乐扣乐扣 
<----------------------------------------------->
```
```sh
$ youdao 您好
<----------------------------------------------->
查询单词： 您好
有道翻译：How do you do

有道词典-基本词典：
发音 [ None ]
shalom
howdy

有道词典-网络释义：
您好  :  Hello guten tag How do you do good afternoon 
您好楼主  :  FFWR 
校长您好  :  Principal Hello President hello 
<----------------------------------------------->

```


```sh
$ youdao hello world
<----------------------------------------------->
查询单词： hello
有道翻译：你好

有道词典-基本词典：
发音 [ həˈləʊ ]
英式发音 [ həˈləʊ ] 	 美式发音 [ helˈō ]
int. 喂；哈罗
n. 表示问候， 惊奇或唤起注意时的用语
n. (Hello)人名；(法)埃洛

有道词典-网络释义：
Hello  :  你好 您好 哈啰 喂 
Hello Kitty  :  凯蒂猫 昵称 匿称 最想当的商品代言人 
Hello Bebe  :  哈乐哈乐 乐扣乐扣 
<----------------------------------------------->
<----------------------------------------------->
查询单词： world
有道翻译：世界

有道词典-基本词典：
发音 [ wɜːld ]
英式发音 [ wɜːld ] 	 美式发音 [ wɝld ]
n. 世界；领域；世俗；全人类；物质生活

有道词典-网络释义：
World  :  世界 界 天下 世上 
world war  :  世界大战 第一次世界大战 僵尸世界大战 末日之战 
My World  :  我的小小世界 我的世界 自一方 自己的世界 
<----------------------------------------------->
```

## Uninstall

### pip

```
sudo pip uninstall youdao_simple
```

### setup.py

```sh
$ sudo python setup.py install --record=/tmp/filelist
# this file will record all the installed files

$ cat /tmp/filelist | sudo xargs rm -rf
```
