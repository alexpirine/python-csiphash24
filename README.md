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
