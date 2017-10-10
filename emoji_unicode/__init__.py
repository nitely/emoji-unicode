# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .pattern import RE_PATTERN_TEMPLATE
from .parser import replace, normalize
from .models import Emoji

__version__ = '0.4'

__all__ = [
    'RE_PATTERN_TEMPLATE',
    'replace',
    'normalize',
    'Emoji'
]
