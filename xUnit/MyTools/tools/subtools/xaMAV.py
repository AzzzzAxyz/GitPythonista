#coding: utf-8

'''

'''

def _single_lst(lst):
	if None in lst:return None
	retD=sum(lst)/len(lst)
	return retD

def _calc(lst,num):
	retD=[None]*(num-1)
	index=range(num,len(lst)+1)
	d=[_single_lst(lst[i-num:i]) for i in index]
	return d+retD

class MAV (object):
	def __init__(self,lst):
		self.data=lst
	
	def by_num(self,num):
		retD=_calc(self.data,num)
		return retD


if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	
	cls=MAV(lst)
	[print(i,l) for i,l in zip(lst,cls.by_num(3))]
	
	
	
	print('main end')
	
