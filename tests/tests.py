# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
import logging
import os
import json
import io

from emoji_unicode import replace, normalize, Emoji
from emoji_unicode.utils import code_point_to_unicode, unicode_to_code_point
from emoji_unicode import data_parser


logging.disable(logging.CRITICAL)

DIR = os.path.dirname(__file__)
FIXTURES = os.path.join(DIR, 'fixtures')
EMOJI_PRETTY_JSON = None


def _get_emoji_pretty():
    global EMOJI_PRETTY_JSON

    if EMOJI_PRETTY_JSON is not None:
        return EMOJI_PRETTY_JSON

    with io.open(os.path.join(FIXTURES, 'emoji_pretty.json'), encoding='utf-8') as fh:
        EMOJI_PRETTY_JSON = fh.read()

    return EMOJI_PRETTY_JSON


def get_emoji_pretty():
    return json.loads(_get_emoji_pretty())


def code_points_to_unicode(code_points):
    return ''.join(
        code_point_to_unicode(p)
        for p in code_points.split('-')
    )


def get_emojis(include_skin_variations=True, include_variations=True):
    # todo: include variations (emoji + emo_variation), android doesn't use them, check iOS
    emojis = []

    for e in get_emoji_pretty():
        emojis.append({
            'unicode': code_points_to_unicode(e['unified']),
            'code_point': e['unified'],
            'short_name': e['short_name']
        })

        if include_skin_variations:
            emojis.extend(
                {
                    'unicode': code_points_to_unicode(point),
                    'code_point': point,
                    'short_name': e['short_name']
                }
                for point in e.get('skin_variations', {}).keys()
            )

        if include_variations:
            emojis.extend(
                {
                    'unicode': code_points_to_unicode(point),
                    'code_point': point,
                    'short_name': e['short_name']
                }
                for point in e.get('variations', [])
            )

    return emojis


def get_emojis_unicode(**kw):
    return [e['unicode'] for e in get_emojis(**kw)]


class MetaTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_code_points_to_unicode(self):
        self.assertEqual(
            code_points_to_unicode('1F58B-1F58B-1F58B'),
            '\U0001f58b\U0001f58b\U0001f58b'
        )

    def test_get_emojis(self):
        self.assertEqual(len(get_emojis()), 1736)
        self.assertEqual(len(get_emojis(include_skin_variations=False)), 1416)
        self.assertEqual(len(get_emojis(include_variations=False)), 1619)

    def test_get_emojis_unicode(self):
        self.assertEqual(len(get_emojis_unicode()), 1736)
        self.assertEqual(len(get_emojis_unicode(include_skin_variations=False)), 1416)
        self.assertEqual(len(get_emojis(include_variations=False)), 1619)


class UtilsTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_code_point_to_unicode(self):
        self.assertEqual(
            code_point_to_unicode('1F58B'),
            '\U0001f58b'
        )

    def test_unicode_to_code_point(self):
        self.assertEqual(
            unicode_to_code_point('\U0001f58b'),
            '1F58B'.lower()
        )


class ModelEmojiTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_unicode(self):
        emoji = Emoji(unicode='foo')
        self.assertEqual(emoji.unicode, 'foo')

    def test_code_points(self):
        emoji = Emoji(unicode='\U0001f58b\U0001f58b\U0001f58b\uFE0F\u200D')
        self.assertEqual(emoji.code_points, '1F58B-1F58B-1F58B'.lower())

    def test_as_map(self):
        emoji = Emoji(unicode='\U0001f58b\U0001f58b\U0001f58b\uFE0F\u200D')
        self.assertEqual(
            emoji.as_map(),
            [('\U0001f58b', '1f58b'), ('\U0001f58b', '1f58b'), ('\U0001f58b', '1f58b')]
        )


class ParserTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_replace(self):
        """
        It should replace all emojis
        """
        emojis = get_emojis()

        # With no spaces will fail due to fitzpatrick tone being a modifier and also a emoji
        txt = ' '.join(get_emojis_unicode())
        txt_code_points = ' '.join(normalize(e['code_point']) for e in emojis)
        res = replace(txt, lambda emoji: emoji.code_points)
        self.assertEqual(res, txt_code_points)

    def test_replace_with_no_fitz(self):
        """
        It should replace no-spaced emojis, excluding fitzpatrick tone emojis
        """
        emojis = get_emojis()
        txt = ''.join(
            e['unicode']
            for e in emojis
            if 'skin-tone' not in e['short_name']
        )
        txt_code_points = ''.join(
            normalize(e['code_point'])
            for e in emojis
            if 'skin-tone' not in e['short_name']
        )
        res = replace(txt, lambda emoji: emoji.code_points)
        self.assertEqual(res, txt_code_points)

    def test_replace_remove(self):
        txt = ''.join(get_emojis_unicode())
        res = replace(txt, lambda emoji: '')
        self.assertEqual(res, '')

    def test_replace_digits(self):
        """
        It should not match single digits
        """
        txt = '#*0123456789'
        res = replace(txt, lambda emoji: '')
        self.assertEqual(res, txt)

    def test_replace_text_variations(self):
        """
        It should not match emojis with text variation
        """
        txt = '\u203C\uFE0E'
        res = replace(txt, lambda emoji: '')
        self.assertEqual(res, txt)

    def test_normalize(self):
        self.assertEqual(normalize('00A900'), 'a900')

    def test_normalize_variations(self):
        self.assertEqual(normalize('00A9-FE0F-200D-F00'), 'a9-f00')

    def test_normalize_separator(self):
        self.assertEqual(normalize('00A9_FE0F_200D_F00', separator='_'), 'a9_f00')


class DataParserTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse(self):
        res = set(data_parser.parse())
        self.assertTrue('\u00A9' in res)
        self.assertTrue('\u2194-\u2199' in res)  # range

    def test_read_template(self):
        template = data_parser.read_template()
        self.assertTrue('{{code_points}}' in template)
        self.assertTrue('RE_PATTERN_TEMPLATE' in template)

    def test_render_template(self):
        code_points = data_parser.parse()
        template = data_parser.read_template()
        rendered_template = data_parser.render_template(template, code_points)
        self.assertTrue('{{code_points}}' not in rendered_template)
        self.assertTrue('RE_PATTERN_TEMPLATE' in rendered_template)
