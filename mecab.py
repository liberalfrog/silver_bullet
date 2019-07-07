# -*- coding: utf-8 -*-

import sys
import MeCab
m = MeCab.Tagger("-Ochasen")
print(m.parse("安倍晋三首相は、国会で施政方針演説を行った。"))
