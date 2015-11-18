#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import sys


def start():
    argv = ['emoji-unicode', 'discover']

    if len(sys.argv) > 1:
        argv = sys.argv

    unittest.main(module=None, argv=argv)


if __name__ == '__main__':
    start()
