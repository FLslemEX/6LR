#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = {1: 'one', 2: 'two', 3: 'three'}
    new_A = dict((v, k) for k, v in A.items())
    print(A, new_A, sep='\n')
