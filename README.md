# langua
A faster port of  https://code.google.com/archive/p/language-detection/ in Python

Installation
============

    $ pip install langua

Supported Python versions 2.7, 3.4+.


Languages
=========

``langua`` supports 55 languages out of the box ([ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)):

    af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
    hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
    pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw

Basic usage
===========

To detect the language of the text:

```python
>>> from langua import Predict
>>> p = Predict()
>>> p.get_lang("Mother")
'en'
>>> p.get_lang(u"தாய்")
'ta'
>>> p.get_lang(u"അമ്മ")
'ml'
```

Benchmark Results
==================

```python
>>> from langua import Predict
>>> p = Predict()
>>> %%timeit
   ...: p.get_lang(u"ഇംഗ്ലീഷ്")
   ...:
1000 loops, best of 3: 721 µs per loop


>>> from langdetect import detect
>>> %%timeit
   ...: detect(u"ഇംഗ്ലീഷ്")
1000 loops, best of 3: 1.07 ms per loop

```


How to add new language?
========================

You need to create a new language profile. The easiest way to do it is to use the [langdetect.jar](https://github.com/shuyo/language-detection/raw/master/lib/langdetect.jar) tool, which can generate language profiles from Wikipedia abstract database files or plain text.

Wikipedia abstract database files can be retrieved from "Wikipedia Downloads" ([http://download.wikimedia.org/](http://download.wikimedia.org/)). They form '(language code)wiki-(version)-abstract.xml' (e.g. 'enwiki-20101004-abstract.xml' ).

usage: ``java -jar langdetect.jar --genprofile -d [directory path] [language codes]``

- Specify the directory which has abstract databases by -d option.
- This tool can handle gzip compressed file.

Remark: The database filename in Chinese is like 'zhwiki-(version)-abstract-zh-cn.xml' or zhwiki-(version)-abstract-zh-tw.xml', so that it must be modified 'zh-cnwiki-(version)-abstract.xml' or 'zh-twwiki-(version)-abstract.xml'.

To generate language profile from a plain text, use the genprofile-text command.

usage: ``java -jar langdetect.jar --genprofile-text -l [language code] [text file path]``

For more details see [language-detection Wiki](https://code.google.com/archive/p/language-detection/wikis/Tools.wiki).


Original project
================

This is a vectorized modification of [Langdetect](https://github.com/Mimino666/langdetect) . There are some numpy optimizations and other tweaks
which have improved the performance of predicting the language class.

LangDetect was a port of another project called [language-detection](https://code.google.com/p/language-detection/)

Pushing to PyPi
=================

Refer [this](https://packaging.python.org/tutorials/distributing-packages/) 
