import re
# a = 'avafdjlj24jf  \n\t2kalgjf67448jpython alkfknkpython'
# r = re.findall('\s', a)
# print(r)

a = 'hello| i love |python'
rr = re.search('hello(.*)python', a)
print(rr.group(1))
