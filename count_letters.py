#!/usr/bin/env python3
# coding: utf-8

import string
import imp
import sys
imp.reload(sys)
from collections import Counter
import operator

cyrillic = u"АаӘәБбВвГгҒғДдЕеЁёЖжЗзИиЙйКкҚқЛлМмНнҢңОоӨөПпРрСсТтУуҰұҮүФфХхҺһЦцЧчШшЩщЪъЫыІіЬьЭэЮюЯя"

ascii_lowercase = cyrillic.lower()
with open("in.txt","r") as in_file:
    with open("counters.txt","a") as out_file:
        c = Counter(letter for line in in_file
                  for letter in line.lower() 
                  if letter in ascii_lowercase)
        sorted = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
        for letter, repetitions in sorted:
            print(letter, repetitions, end="\n", file=out_file)