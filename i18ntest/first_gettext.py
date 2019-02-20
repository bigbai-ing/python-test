#!/usr/bin/env python
# -*- coding:utf-8 -*-

import gettext

t = gettext.translation("first", "locale", fallback=False,)
#t = gettext.translation("first", "locale", fallback=True,)
_ = t.gettext #一般使用_
print(_('This message is we want to tranlate.'))

