#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    school = {'1а': 25, '1б': 24, '1в': 22, '2а': 22, '2б': 23, '3а': 19, '3б': 15, '3в': 18, '4а': 23, '4б': 20, '5а': 22, '5б': 21, '5в': 24, '6а': 19, '6б': 17, '7а': 21, '7б': 18, '8а': 20, '8б': 20, '9а': 19, '9б': 20,  '10а': 16, '10б': 19, '11а': 19, '11б': 17}
    school['3а'] = 21
    school['6в'] = 15
    del school['5в']
    students = 0
    for i, k in enumerate(school):
        students += school[k]
    print("Общее число учащихся в школе: ", students)