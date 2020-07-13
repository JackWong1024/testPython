import curses
from random import randrange,choice
from collections import defaultdict
actions=['Up','Left','Down','Right','Restart','Exit']
#ord()函数以一个字符作为参数,返回参数对应的ASCII数值,以便于和后面捕捉的键位关联
letter_codes=[ord(ch) for ch in 'WASDRQwasdqr']
#输入与行为关联
actions_dict = dict(zip(letter_codes, actions * 2))