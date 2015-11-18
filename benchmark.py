#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import re
import functools
import timeit

from emoji_unicode import data_parser
from emoji_unicode.parser import replace, RE_PATTERN_TEMPLATE


if __name__ == '__main__':
    data_parser.generate_pattern_file()

    txt = '⛽'
    txt *= 10000
    print('emoji.replace()')
    print('text len: {}'.format(len(txt)))
    print(timeit.timeit(functools.partial(replace, txt, lambda x: ''), number=1))

    print('\nre.sub() (raw match)')
    print('text len: {}'.format(len(txt)))
    pattern = re.compile(RE_PATTERN_TEMPLATE)
    print(timeit.timeit(functools.partial(re.sub, pattern, lambda x: '', txt), number=1))

    txt = 'a'
    txt *= 10000
    print('\nText with no emojis')
    print('emoji.replace()')
    print('text len: {}'.format(len(txt)))
    print(timeit.timeit(functools.partial(replace, txt, lambda x: ''), number=1))
