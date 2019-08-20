#打印99乘法表
# -*- coding: utf-8 -*-
for i in range(1,10):
    print (i-1)*("       "),
    for j in range(i,10):
        line='{}*{}={:<2}'.format(j,i,j*i)
        print line,
    print ""