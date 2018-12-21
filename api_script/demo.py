# coding:utf-8

from multiprocessing import Process, Lock

def f(x,y):
	return x*y

if __name__ == '__main__':
	x =1
	for num in range(2):
		n =Process(target=f, args=(x, num)).start()
		print(n)
