Summary
=======

Create windows shortcuts (`.lnk` files) from anywhere, including linux..

Python adaptation of some bash/C from
http://www.mamachine.org/mslink/index.en.html that seems to work. I have no
clue how.. All credits go to that author for deciphering the specifications
laid out by Microsoft here:
http://msdn.microsoft.com/en-us/library/dd871305.aspx

This currently is able to at least create local windows shortcuts.

Installation
============

To install: ``pip install swinlnk``

Example
=======

```python
from swinlnk.swinlnk import SWinLnk

swl = SWinLnk()

swl.create_lnk('W:\\Foo\\Bar', '/mnt/win_share/playground/Bar_winlink.lnk')
```
