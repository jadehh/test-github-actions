#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : test.py
# @Author   : jade
# @Date     : 2023/3/10 13:58
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
def test_print_chinese():
    import sys
    print("sys.stdout.encoding:{}".format(sys.stdout.encoding))
    print("中文输出")
if __name__ == '__main__':
    test_print_chinese()