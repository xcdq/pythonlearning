filename = 'pyy/program.txt'
with open(filename, 'a')as fb:
    """讀取模式r 寫入模式w 附加模式a 讀取寫入r+"""
    fb.write(" because she is beautiful.\n")
    print('ok')
