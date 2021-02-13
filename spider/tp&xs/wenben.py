import re


def changebq(txt):
    txt = txt.replace('<br/>', '\n')
    txt = txt.replace('<br />', '\n')
    txt = txt.replace('</p>', '\n')
    txt = txt.replace('<p>', '')
    txt = txt.replace('&nbsp;', '')
    txt = txt.replace('<BR>', '\n')
    txt = txt.replace('<br>', '')
    txt = txt.replace('&hellip;', '')
    txt = txt.replace('&hellip;', '')
    txt = txt.replace('&hellip;', '')

    return txt
