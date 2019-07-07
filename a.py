# -*- coding: utf-8 -*-

import sys
import MeCab
m = MeCab.Tagger ("-Ochasen")
m.parse("")
m.parse("")
node = m.parseToNode("お前が見たのを見たぞ")
while node:
    print(node.surface)
    node = node.next
