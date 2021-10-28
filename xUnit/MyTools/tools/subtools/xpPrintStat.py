#coding: utf-8

import matplotlib.pyplot as plt
import xcToolList as xl
import statistics

'''

'''


def sigma(lst):
	d_without_None=xl.remove_None(lst)
	answer=statistics.stdev(d_without_None)
	print(f'std :{answer:.3f}')
	return answer


def average(lst):
	d_without_None=xl.remove_None(lst)
	answer=statistics.mean(d_without_None)
	print(f'ave :{answer:.3f}')
	return answer



if __name__ == '__main__':
	print ('main test')
	
	d=[l*0.97 for l in range(10)]+[None,None]+[3.33]
	average(d)
	sigma(d)

	
	
	print('main end')
