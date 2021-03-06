
[![PyPI](https://img.shields.io/pypi/v/csiphash24.svg)](https://pypi.python.org/pypi/csiphash24)

# python-csiphash24

SipHash-2-4 implementation, CFFI-wrapped for Python.

It just works. If you have Python ≥ 3.6.

Inspired by https://github.com/majek/csiphash and https://github.com/zacharyvoase/python-csiphash.

## How to install

```console
$ pip install csiphash24
```

## How to use

```python
>>> from binascii import hexlify
>>> from csiphash24 import siphash24
>>> hexlify(siphash24(b'0123456789abcdef', b'hello'))
b'95a3a242a9dd85d1'
```

## Is it fast ?

On my late-2016 MacBook Pro, hashing a 256-bytes message takes less than a microsecond on average (about 780 nanoseconds to be precise).

## What implementaiton is this?

To be honest, I'm not sure. I tried several implementations and they weren't compatible with the device I was working with. This one seems to do the job. So, it might work for you too.
