# coding:utf-8

a = 0
b = 1

for i in range(10):
	a += 1
	b = a+b
	print("b: "+str(b))