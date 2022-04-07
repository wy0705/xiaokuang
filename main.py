# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

import shutil
import os
from datetime import time


def sentence_filter(keywords, text):
    return re.sub("|".join(keywords), "***", text)

def print_hi(speak):
    dirty=['苍井空','暴力男','fuck']
    print("方法一：")
    print(sentence_filter(dirty, speak))
    for i in dirty:
        speak = speak.replace(i, '***')
    print("方法二")
    print(speak)


def print_():
    print("------------------------------")

def print_in(speak):
    print(speak)

def sum(a,b,c):
    print(int(a)+int(b)+int(c))

def ave(a,b,c):
    print((int(a)+int(b)+int(c))/3)

def copy_():
    ff = open("copy.txt", "a+")
    shutil.copyfile("gushi.txt", "copy.txt")
    ff.close()
    print("复制完毕")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    txtName = "gushi.txt"
    new_context = "相思\n王维\n红豆生南国\n春来发几枝\n愿君多采撷\n此物最相思\n"
    f = open(txtName, "a+")
    f.write(new_context)
    f.close()

    copy_()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
