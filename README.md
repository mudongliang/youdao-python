# youdao-python
youdao dictionary implemented in python

## Install

### pip

```
sudo pip install youdao_simple
```

### python setup.py

```sh
$ git clone https://github.com/MintCN/youdao-python
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
hello
有道翻译 : 
你好

有道词典-基本词典 : 
英式发音 [ həˈləʊ ] 	美式发音 [ həˈlo ]
n. 表示问候， 惊奇或唤起注意时的用语
int. 喂；哈罗
n. (Hello)人名；(法)埃洛

有道词典-网络释义 : 
Hello  :  你好 您好 hello 
Hello Kitty  :  凯蒂猫 昵称 匿称 
Hello Bebe  :  哈乐哈乐 乐扣乐扣

```

```sh
$ youdao hello world
查询单词： hello
有道翻译 : 
你好

有道词典-基本词典 : 
英式发音 [ həˈləʊ ] 	 美式发音 [ həˈlo ]
n. 表示问候， 惊奇或唤起注意时的用语
int. 喂；哈罗
n. (Hello)人名；(法)埃洛

有道词典-网络释义 : 
Hello  :  你好 您好 hello 
Hello Kitty  :  凯蒂猫 昵称 匿称 
Hello Bebe  :  哈乐哈乐 乐扣乐扣 

查询单词： world
有道翻译 : 
世界

有道词典-基本词典 : 
英式发音 [ wɜːld ] 	 美式发音 [ wɝld ]
n. 世界；领域；世俗；全人类；物质生活

有道词典-网络释义 : 
World  :  世界 世界 天下 
My World  :  我的小小世界 我的世界 自一方 
World Record  :  世界纪录 世界纪录 世界之最 

```

## Uninstall

### pip

```
sudo pip uninstall youdao_simple
```

### python setup.py

```sh
$ sudo python setup.py install --record=/tmp/filelist
# this file will record all the installed files

$ cat /tmp/filelist | sudo xargs rm -rf
```
