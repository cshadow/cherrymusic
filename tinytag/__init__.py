#!/usr/bin/python
# -*- coding: utf-8 -*-
from .tinytag import TinyTag, ID3, Ogg, Wave, Flac


__version__ = '0.10.1'

if __name__ == '__main__':
    print(TinyTag.get(sys.argv[1]))