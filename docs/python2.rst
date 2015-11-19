Python 2 Support
================

Python 2 is by default build with *narrow* unicode characters support, this means
it does not support unicode code points above ``0xffff`` which most emojis are.
Python +3.3 does not suffer from this.

Requirements
------------

To support `wide unicode characters <https://www.python.org/dev/peps/pep-0261/>`_,
python 2.7 must be build from source with ``--enable-unicode=ucs4`` flag.

To find if python 2 has support for *wide* unicode characters, run::

    $ python
    >>> import sys
    >>> 'Is this a wide-build? {}'.format(sys.maxunicode > 65536)

