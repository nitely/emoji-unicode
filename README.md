# emoji-unicode

[![Build Status](https://img.shields.io/travis/nitely/emoji-unicode.svg?style=flat-square)](https://travis-ci.org/nitely/emoji-unicode)
[![Coverage Status](https://img.shields.io/coveralls/nitely/emoji-unicode.svg?style=flat-square)](https://coveralls.io/r/nitely/emoji-unicode)
[![pypi](https://img.shields.io/pypi/v/emoji-unicode.svg?style=flat-square)](https://pypi.python.org/pypi/emoji-unicode)
[![licence](https://img.shields.io/pypi/l/emoji-unicode.svg?style=flat-square)](https://raw.githubusercontent.com/nitely/emoji-unicode/master/LICENSE)

Replace unicode emojis by its corresponding image representation. Supports *Unicode 8* standard.

## Compatibility

* Python 2.7, 3.3, 3.4 and 3.5 (recommended)

## Install

```
$ pip install emoji-unicode
```

## Usage

### Replace

[docs](http://emoji-unicode.readthedocs.org/en/latest/api.html#emoji_unicode.replace)

```python
emoji_unicode.replace(
    'Time to ⛽',
    lambda e: '<img src="{filename}.svg" alt="{raw}">'.format(filename=e.code_points, raw=e.unicode)
)
# Time to <img src="26fd.svg" alt="⛽">
```

> Note: the [Emoji.code_points](http://emoji-unicode.readthedocs.org/en/latest/api.html#emoji_unicode.Emoji.code_points) are normalized.

### Normalize

This function removes optional characters that may appear depending on
the input source (Android, iOS, etc). For example the emoji variation `\\uFE0F`
may (or may not) appear in between a emoji and a skin tone modifier,
making the code points to be different. It should be used
to rename the image files.

[docs](http://emoji-unicode.readthedocs.org/en/latest/api.html#emoji_unicode.normalize)

```python
emoji_unicode.normalize('1F468-200D-2764-FE0F-200D-1F468')
# 1f468-2764-1f468
```

### Replace (advanced)

```python
PATTERN = re.compile(emoji_unicode.RE_PATTERN_TEMPLATE)


def match_handler(m):
    e = emoji_unicode.Emoji(unicode=m.group('emoji'))
    return '<img src="{filename}.svg" alt="{raw}">'.format(
        filename=e.code_points,
        raw=e.unicode
    )


re.sub(PATTERN, match_handler, 'Time to ⛽')
# Time to <img src="26fd.svg" alt="⛽">
```

## Docs

[docs](http://emoji-unicode.readthedocs.org/en/latest/)

## Dev

The `./emoji_unicode/pattern.py` file is generated
by parsing the `./emoji_unicode/emoji-data.txt` file,
then putting the output in a in-memory copy of
`./emoji_unicode/pattern_template.py`, and lastly
writing the result into `pattern.py`.

To generate the `pattern.py` fie, run:

```
$ python ./build.py
```

## Tests

```
$ python ./runtests.py
```

## Benchmark

This will run some silly benchmarks.

```
$ python ./benchmark.py
```

Here is the output on my machine:

```
emoji.replace()
text len: 10000
0.01640868396498263

re.sub() (raw match)
text len: 10000
0.005225047003477812

Text with no emojis
emoji.replace()
text len: 10000
0.0014624089817516506
```

## Acknowledgments

Thanks to [iamcal/emoji-data](https://github.com/iamcal/emoji-data)
for maintaining an incredible source of emojis that allowed me
to make a robust test suite.

## License
MIT
