youdao-python
=============

youdao dictionary implemented in python

Install
-------

pip
~~~

::

    sudo pip install youdao_simple

python setup.py
~~~~~~~~~~~~~~~

.. code:: sh

    $ git clone https://github.com/mudongliang/youdao-python
    $ cd youdao-python
    $ sudo python setup.py install

Usage
-----

.. code:: sh

    $ youdao
    No word to translate

    $ youdao hello
    hello
    有道翻译 : 
    你好

    有道词典-基本词典 : 
    英式发音 [ həˈləʊ ]     美式发音 [ həˈlo ]
    n. 表示问候， 惊奇或唤起注意时的用语
    int. 喂；哈罗
    n. (Hello)人名；(法)埃洛

    有道词典-网络释义 : 
    Hello  :  你好 您好 hello 
    Hello Kitty  :  凯蒂猫 昵称 匿称 
    Hello Bebe  :  哈乐哈乐 乐扣乐扣

Uninstall
---------

pip
~~~

::

    sudo pip uninstall youdao_simple

python setup.py
~~~~~~~~~~~~~~~

.. code:: sh

    $ sudo python setup.py install --record=/tmp/filelist
    # this file will record all the 

    $ cat /tmp/filelist | sudo xargs rm -rf
