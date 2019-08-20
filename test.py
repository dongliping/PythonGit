#不同方法打印99乘法表
# -*- coding: utf-8 -*-
for i in range(1,10):
    print (i-1)*("       "),
    for j in range(i,10):
        line='{}*{}={:<2}'.format(j,i,j*i)
        print line,
    print ""


for i in range(1,10):
    for j in range(1, 10):
        if i>j:
            line= '{} {} {:<2}'.format(" "," "," ")
        else:
            line = '{}*{}={:<2}'.format(i, j, i * j)
        print line,
    print ""	


#打印菱形
for i in range(-3,4):
    if i<0:
        j=-i
    else:
        j=i
    print " "*j+"*"*(7-2*j) 
	
#打印镂空菱形
for i in range(-3,4):
    if i==-3 or i==3:
        count=abs(i)
        print " "*count+"*"
    else:
        count=abs(i)
        print " "*count+"*"+" "*(5-2*count)+"*"
		
#打印特殊菱形
for i in range(-3,4):
	if i<0:
		a=abs(i)-1
		print " "*a,
		print "*"*(3-a)
	elif i>0:
		print " "*3+"*"*(4-i)
	else:
		print "*"*7		
		
#输入5个数字，并用冒泡排序
nums=[]
while len(nums)<5:
	num=raw_input("enter a num").strip().lstrip('0')
	if not num.isdigit():
		continue
	print "the lentgh of {} is {}".format(num,len(nums))
	nums.append(int(num))
	
for i in range(len(nums)):
	for j in range(len(nums)-i-1):
		flag=False
		if nums[j]>nums[j+1]:
			nums[j],nums[j+1]=nums[j+1],nums[j]
			flag=True
	if not flag:
		break
print nums