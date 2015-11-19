# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .utils import unicode_to_code_point
from .pattern import EMO_VARIATION, ZWJ

JOINER_CHARS = {EMO_VARIATION, ZWJ}


class Emoji(object):
    """
    Emoji is used in the process of :py:func:`.replace` unicode emojis in a text

    :param str unicode: Unicode emoji
    """
    def __init__(self, unicode):
        self.unicode = unicode
        self._code_points = None
        self._map = None

    @property
    def code_points(self):
        """
        Code points representing the unicode emoji,\
        the result is normalized as by :py:func:`.normalize`

        :getter: Code points representing the emoji,\
        with no joiner chars and lower cased, ie: 1f3c3-1f3fc
        :type: str
        """
        if self._code_points is not None:
            return self._code_points

        self._code_points = '-'.join(
            unicode_to_code_point(u)
            for u in self.unicode
            if u not in JOINER_CHARS
        )

        return self._code_points

    def as_map(self):
        """
        A map containing the individual unicode chars and code points.\
        The code points are normalized as by :py:func:`.normalize`

        :return: Sequence of tuples of the form [(unicode, code_point)]
        :rtype: list
        """
        if self._map is not None:
            return self._map

        self._map = [
            (u, unicode_to_code_point(u))
            for u in self.unicode
            if u not in JOINER_CHARS
        ]

        return self._map
