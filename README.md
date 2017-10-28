# langua
A faster port of  https://code.google.com/archive/p/language-detection/ in Python


Basic usage
===========

To detect the language of the text:

```python
>>> from langua import DetectLang
>>> dt = DetectLang()
>>> dt.detect("War doesn't show who's right, just who's left.")
'en'
>>> dt.detect("Ein, zwei, drei, vier")
'de'
```