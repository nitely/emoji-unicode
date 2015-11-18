# -*- coding: utf-8 -*-

from __future__ import unicode_literals


CODE_POINTS = '\xa9\xae\u203c\u2049\u2122\u2139\u2194-\u2199\u21a9-\u21aa\u231a-\u231b\u2328\u23cf\u23e9-\u23f3\u23f8-\u23fa\u24c2\u25aa-\u25ab\u25b6\u25c0\u25fb-\u25fe\u2600-\u2604\u260e\u2611\u2614-\u2615\u2618\u261d\u2620\u2622-\u2623\u2626\u262a\u262e-\u262f\u2638-\u263a\u2648-\u2653\u2660\u2663\u2665-\u2666\u2668\u267b\u267f\u2692-\u2694\u2696-\u2697\u2699\u269b-\u269c\u26a0-\u26a1\u26aa-\u26ab\u26b0-\u26b1\u26bd-\u26be\u26c4-\u26c5\u26c8\u26ce-\u26cf\u26d1\u26d3-\u26d4\u26e9-\u26ea\u26f0-\u26f5\u26f7-\u26fa\u26fd\u2702\u2705\u2708-\u270d\u270f\u2712\u2714\u2716\u271d\u2721\u2728\u2733-\u2734\u2744\u2747\u274c\u274e\u2753-\u2755\u2757\u2763-\u2764\u2795-\u2797\u27a1\u27b0\u27bf\u2934-\u2935\u2b05-\u2b07\u2b1b-\u2b1c\u2b50\u2b55\u3030\u303d\u3297\u3299\U0001f004\U0001f0cf\U0001f170-\U0001f171\U0001f17e-\U0001f17f\U0001f18e\U0001f191-\U0001f19a\U0001f1e6-\U0001f1ff\U0001f201-\U0001f202\U0001f21a\U0001f22f\U0001f232-\U0001f23a\U0001f250-\U0001f251\U0001f300-\U0001f321\U0001f324-\U0001f393\U0001f396-\U0001f397\U0001f399-\U0001f39b\U0001f39e-\U0001f3f0\U0001f3f3-\U0001f3f5\U0001f3f7-\U0001f4fd\U0001f4ff-\U0001f53d\U0001f549-\U0001f54e\U0001f550-\U0001f567\U0001f56f-\U0001f570\U0001f573-\U0001f579\U0001f587\U0001f58a-\U0001f58d\U0001f590\U0001f595-\U0001f596\U0001f5a5\U0001f5a8\U0001f5b1-\U0001f5b2\U0001f5bc\U0001f5c2-\U0001f5c4\U0001f5d1-\U0001f5d3\U0001f5dc-\U0001f5de\U0001f5e1\U0001f5e3\U0001f5e8\U0001f5ef\U0001f5f3\U0001f5fa-\U0001f64f\U0001f680-\U0001f6c5\U0001f6cb-\U0001f6d0\U0001f6e0-\U0001f6e5\U0001f6e9\U0001f6eb-\U0001f6ec\U0001f6f0\U0001f6f3\U0001f910-\U0001f918\U0001f980-\U0001f984\U0001f9c0'  # Template string

TXT_VARIATION = '\uFE0E'
EMO_VARIATION = '\uFE0F'
FITZ_MODIFIER = '\U0001F3FB-\U0001F3FF'
KC_MODIFIER = '\u20E3'
ZWJ = '\u200D'
FLAGS = '\U0001F1E6-\U0001F1FF'
KEY_CAPS = '0-9\*#'

RE_PATTERN_TEMPLATE = (
    r'(?P<emoji>'
        r'(?:'
            r'(?:[%(key_caps)s](?:%(emo_variation)s)?%(kc_modifier)s)'
            r'|'
            r'(?:[%(flags)s]){2}'
            r'|'
            r'(?:[%(emojis)s])(?!%(txt_variation)s)'
        r')'
        r'(?:'
            r'(?:(?:%(emo_variation)s)?(?:[%(fitz_modifier)s]))'  # fitzpatrick modifier
            r'|'
            r'(?:(?:%(emo_variation)s)?(?:[%(zwj)s])(?:.)){1,4}'  # Multi glyphs (up to 4)
            r'|'
            r'(?:%(emo_variation)s)'  # Emoji variation
        r')?'
    r')'
) % {
    'emojis': CODE_POINTS,
    'txt_variation': TXT_VARIATION,
    'emo_variation': EMO_VARIATION,
    'fitz_modifier': FITZ_MODIFIER,
    'zwj': ZWJ,
    'flags': FLAGS,
    'kc_modifier': KC_MODIFIER,
    'key_caps': KEY_CAPS
}  # noqa
