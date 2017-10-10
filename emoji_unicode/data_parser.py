# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# This script is base on:
# http://www.unicode.org/Public/emoji/latest/emoji-data.txt
# and (Unicode 8.0 emojis)
# http://unicode.org/reports/tr51/

# Invisible variation selectors:
# U+FE0E for a text presentation
# U+FE0F for an emoji presentation
#
# U+200D ZERO WIDTH JOINER (ZWJ) can be used between the elements
# of a sequence of characters to indicate that a single glyph
# should be presented if available.
#
# EMOJI MODIFIER FITZPATRICK
# U+1F3FB..U+1F3FF
#
# Variation selector (U+FE0F) may or may not be between Fitz modifier and the emoji
#
# Regional indicators:
# 1F1E6..1F1FF
#
# Mark modifiers (ie: square-digits)
# 20E0 enclosing_circle_backlash
# 20E3 enclosing_keycap
#
# emoji sequence:
# (emoji_modifier_base | emoji_base_variation_sequence) | emoji_modifier
#
# emoji core sequence:
# emoji_modifier_base | emoji_base_variation_sequence | emoji_modifier | emoji_flag_sequence

import os
import io

from .utils import code_point_to_unicode


DIR = os.path.dirname(__file__)


def escape_unicode(txt):
    return txt \
        .encode('unicode_escape') \
        .replace(b'\\', b'\\\\') \
        .decode('unicode_escape')


def _parse(line):
    code_point = line.split(';', 1)[0]
    return '-'.join(
        code_point_to_unicode(c)
        for c in code_point.strip().split('..')
    )


EMOJI_EXCLUDE = {str(n) for n in range(0, 10)} | {'#', '*'}


def parse():
    with io.open(os.path.join(DIR, 'emoji-data.txt'), mode='r', encoding='utf-8') as fh:
        cps = []

        for line in fh.readlines():
            if line.startswith('#'):
                continue

            cp = _parse(line)

            if cp.split('-')[0] in EMOJI_EXCLUDE:
                continue

            cps.append(cp)

        return cps


def read_template():
    with io.open(os.path.join(DIR, 'pattern_template.py'), mode='r', encoding='utf-8') as fh:
        return fh.read()


def render_template(template, code_points):
    code_points = escape_unicode(''.join(code_points))
    return template.replace('{{code_points}}', code_points)


def write_pattern_file(template_rendered):
    with io.open(os.path.join(DIR, 'pattern.py'), mode='w', encoding='utf-8') as fh:
        fh.write(template_rendered)


def generate_pattern_file():
    code_points = parse()
    template = read_template()
    template_rendered = render_template(template, code_points)
    write_pattern_file(template_rendered)


